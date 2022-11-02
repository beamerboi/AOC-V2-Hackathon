from django.db import models
from AOCV2 import settings


class Contact(models.Model):
    subject = models.CharField(max_length=30)
    message = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.subject