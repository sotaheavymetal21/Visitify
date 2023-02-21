from django.db import models
from django.contrib.auth.models import User


# class Profile(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     website = models.URLField(blank=True)
#     self_introduction = models.TextField(blank=True)
#     free_text = models.TextField(null=True, blank=True)

#     def __str__(self):
#         return self.username