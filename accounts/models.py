from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    skills = models.CharField(max_length=255, null=True, blank=True)
    free_text = models.TextField(null=True, blank=True)

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
    class Meta:
        db_table = "User"