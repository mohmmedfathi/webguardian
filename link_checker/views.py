from django.shortcuts import render
from django.conf import settings
import requests
from services.virustotal_service import VirusTotalService

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
    
    return render(request, 'link_checker/index.html', context)