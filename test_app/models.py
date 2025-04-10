from django.db import models
 
# Create your models here.
from django.conf import settings

class Book(models.Model):
    title = models.CharField(verbose_name = 'タイトル', max_length=64)
    description = models.TextField(verbose_name = '本の説明', blank=True)
    author = models.CharField(verbose_name = '著者', max_length=64)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, verbose_name = '作成者')

    def __str__(self):
        return self.title