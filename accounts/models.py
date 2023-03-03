from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    free_text = models.TextField(null=True, blank=True)  # 自由記入欄