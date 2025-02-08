import re
import speech_recognition as sr
from pydub import AudioSegment
import tempfile
from pathlib import Path

def process_audio_file(audio_file):
    """Processes audio file and extracts the first URL."""
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            input_path = Path(temp_dir) / "input_audio"
            input_path.write_bytes(audio_file.read())
            
            # Convert to WAV format
            audio_segment = AudioSegment.from_file(str(input_path))
            wav_path = Path(temp_dir) / "converted.wav"
            audio_segment.export(wav_path, format="wav", parameters=["-ac", "1"])
            
            # Recognize speech using Google API
            recognizer = sr.Recognizer()
            with sr.AudioFile(str(wav_path)) as source:
                recognizer.adjust_for_ambient_noise(source)
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data, language='en-US')

            return extract_url_from_text(text)
    except sr.UnknownValueError:
        raise ValueError('لم نتمكن من التعرف على الكلام')
    except Exception:
        raise ValueError('حدث خطأ أثناء معالجة الملف الصوتي')

def extract_url_from_text(text):
    """Extracts and cleans the URL from the transcribed text."""
    url_pattern = re.compile(r'http[s]?://\S+|\S+')
    urls = re.findall(url_pattern, text)
    
    # Clean URLs by removing spaces between parts of the URL
    cleaned_urls = [''.join(url.split()) for url in urls]
    
    if not cleaned_urls:
        raise ValueError('لم يتم العثور على رابط في النص المنطوق')

    url = cleaned_urls[0]
    if not re.match(r'^(https?:\/\/)?([\w-]+\.)+[\w-]+(\/[\w-]*)*$', url):
        raise ValueError('الرابط المنطوق غير صالح')

    return url, text
