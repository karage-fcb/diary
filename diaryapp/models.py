from django.db import models
from django.conf import settings

# Create your models here.

class DiaryModel(models.Model):
    date = models.DateField()
    dream = models.CharField(max_length=100)
    event = models.TextField()
    submitter = models.ForeignKey(settings.AUTH_USER_MODEL, models.PROTECT, verbose_name='投稿者')