let isRecording = false;
let mediaRecorder;
let audioStream;
let recordingTimer;
let recordingDuration = 0;
const MAX_RECORDING_TIME = 10; // Maximum recording time in seconds

function updateUI(recording) {
    const recordBtn = document.getElementById('recordBtn');
    const statusDiv = document.getElementById('recordingStatus');
    
    if (recording) {
        recordBtn.innerHTML = '<i class="fas fa-stop"></i>';
        recordBtn.classList.add('btn-danger');
        statusDiv.innerHTML = '<div class="alert alert-info">جارٍ التسجيل: <span id="recordingTime">0</span> ثواني</div>';
    } else {
        recordBtn.innerHTML = '<i class="fas fa-microphone"></i>';
        recordBtn.classList.remove('btn-danger');
        statusDiv.textContent = '';
    }
}

function cleanupRecording() {
    if (recordingTimer) {
        clearInterval(recordingTimer);
        recordingTimer = null;
    }
    if (audioStream) {
        audioStream.getTracks().forEach(track => track.stop());
        audioStream = null;
    }
    recordingDuration = 0;
    isRecording = false;
    updateUI(false);
}
document.getElementById('recordBtn').addEventListener('click', async () => {
    const recordBtn = document.getElementById('recordBtn');
    const statusDiv = document.getElementById('recordingStatus');
    
    if (!isRecording) {
        try {
            audioStream = await navigator.mediaDevices.getUserMedia({ audio: true });
            mediaRecorder = new MediaRecorder(audioStream);
            isRecording = true;
            recordingDuration = 0;
            
            // Start recording timer
            recordingTimer = setInterval(() => {
                recordingDuration++;
                document.getElementById('recordingTime').textContent = recordingDuration;
                
                if (recordingDuration >= MAX_RECORDING_TIME) {
                    if (mediaRecorder.state === 'recording') {
                        mediaRecorder.stop();
                    }
                }
            }, 1000);
            
            mediaRecorder.ondataavailable = async (e) => {
                const audioBlob = new Blob([e.data], { type: 'audio/webm' });
                const formData = new FormData();
                formData.append('audio', audioBlob, 'recording.wav');
                
                statusDiv.innerHTML = '<div class="alert alert-info"><div class="spinner-border spinner-border-sm"></div> جارٍ تحويل الصوت...</div>';
                
                try {
                    const response = await fetch(`${window.location.origin}/process_audio/`, {
                        method: 'POST',
                        body: formData,
                        credentials: 'same-origin',
                        headers: {
                            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                        }
                    });
                    
                    const data = await response.json();
                    
                    if (!response.ok) {
                        throw new Error(data.error || 'فشل في تحويل الصوت');
                    }
                    
                    if (data.transcribed_text) {
                        document.getElementById('urlInput').value = data.transcribed_text;
                        statusDiv.innerHTML = '<div class="alert alert-success">تم التحويل بنجاح</div>';
                        document.getElementById('linkForm').submit();
                    } else {
                        throw new Error('لم يتم استلام نص محول');
                    }
                    
                } catch (error) {
                    console.error('Error:', error);
                    statusDiv.innerHTML = `<div class="alert alert-danger">خطأ: ${error.message}</div>`;
                    recordBtn.innerHTML = '<i class="fas fa-microphone"></i>';
                    recordBtn.classList.remove('btn-danger');
                }
            };

            mediaRecorder.start();
            updateUI(true);

            mediaRecorder.onerror = (event) => {
                console.error('MediaRecorder error:', event.error);
                statusDiv.innerHTML = '<div class="alert alert-danger">خطأ في التسجيل</div>';
                cleanupRecording();
            };

        } catch (error) {
            statusDiv.innerHTML = '<div class="alert alert-danger">السماح باستخدام الميكروفون مطلوب!</div>';
            console.error('خطأ في الوصول للميكروفون:', error);
        }
    } else {
        if (mediaRecorder && mediaRecorder.state === 'recording') {
            mediaRecorder.stop();
        }
        cleanupRecording();
    }
});

// تشغيل الصوت تلقائياً عند وجود نتيجة
document.addEventListener('DOMContentLoaded', () => {
    const audioPlayer = document.querySelector('audio');
    if (audioPlayer) {
        audioPlayer.play().catch(error => {
            console.log('تشغيل الصوت التلقائي معطل:', error);
        });
    }
});

document.getElementById('linkForm').addEventListener('submit', function(e) {
    const urlInput = document.getElementById('urlInput');
    if (urlInput.value.trim() === "") {
        e.preventDefault();
        urlInput.classList.add('is-invalid');
    } else {
        urlInput.classList.remove('is-invalid');
    }
});
