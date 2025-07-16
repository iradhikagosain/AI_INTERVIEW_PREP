from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    generated_questions = models.TextField(null=True, blank=True)  

    def __str__(self):
        return f"{self.user.username} - Resume"
