from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

User = get_user_model()

class LinkScan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField(max_length=500, validators=[URLValidator()])
    is_safe = models.BooleanField(default=False)
    details = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    audio_response = models.FileField(upload_to='audio_responses/%Y/%m/%d/', null=True, blank=True)

    def clean(self):
        if not self.url.startswith(('http://', 'https://')):
            raise ValidationError("الرابط يجب أن يبدأ بـ http:// أو https://")

    def __str__(self):
        return f"فحص {self.url} في {self.created_at}"