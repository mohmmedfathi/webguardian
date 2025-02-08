from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.conf import settings
from django.utils.text import slugify
from django.core.files.storage import default_storage

from services.virustotal_service import VirusTotalService
from services.audio_service import process_audio_file, extract_url_from_text

from gtts import gTTS
import re

@csrf_exempt
def process_audio(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    
    audio_file = request.FILES.get('audio')
    if not audio_file:
        return JsonResponse({'error': 'لم يتم تقديم ملف صوتي'}, status=400)
    
    if not audio_file.content_type.startswith('audio/'):
        return JsonResponse({'error': 'نوع الملف غير مدعوم'}, status=400)
    
    try:
        url, text = process_audio_file(audio_file)
        safety_result = VirusTotalService.check_url_safety(url)
        
        if not safety_result or 'safe' not in safety_result:
            return JsonResponse({'error': 'تعذر الحصول على نتيجة من خدمة الفحص. يرجى المحاولة مرة أخرى لاحقًا.'}, status=500)
        
        return JsonResponse({'success': True, 'transcribed_text': text, 'url': url, 'safety_result': safety_result})
            
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=422)
    except Exception:
        return JsonResponse({'error': 'حدث خطأ أثناء معالجة الملف الصوتي. يرجى المحاولة مرة أخرى لاحقًا.'}, status=500)

def home(request):
    context = {}
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            result = VirusTotalService.check_url_safety(url)
            
            if not result or 'safe' not in result:
                context['error'] = 'تعذر الحصول على نتيجة من خدمة الفحص. يرجى المحاولة مرة أخرى لاحقًا.'
            else:
                context['result'] = {
                    'safe': result['safe'],
                    'message': result['message'],
                    'details': {
                        'harmless': result['details'].get('harmless', 0),
                        'malicious': result['details'].get('malicious', 0),
                        'suspicious': result['details'].get('suspicious', 0)
                    }
                }

                tts_text = "هذا الموقع امن" if result['safe'] else "احترس الموقع ضار"
                tts = gTTS(text=tts_text, lang='ar')
                audio_buffer = ContentFile(b'')
                tts.write_to_fp(audio_buffer)
                audio_filename = f"audio_responses/{slugify(url)}.mp3"
                default_storage.save(audio_filename, audio_buffer)
                context['audio_url'] = f"{settings.MEDIA_URL}{audio_filename}"
    
    return render(request, 'link_checker/index.html', context)
