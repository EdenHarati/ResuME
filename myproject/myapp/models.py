
# models.py

from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    FILE_TYPE_CHOICES = [
        ('CV', 'CV'),
        ('JD', 'Job Description'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    file_type = models.CharField(max_length=2, choices=FILE_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.get_file_type_display()}"



   # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_files')

