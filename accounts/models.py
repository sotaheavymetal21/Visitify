from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    free_text = models.TextField(null=True, blank=True)
    password = models.CharField(max_length=128, default="")

  # リレーションフィールドのrelated_nameを変更する
    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        related_name="user_profiles"
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        related_name="user_profiles"
    )