from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class MyStudy(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    totalMember = models.CharField(max_length=200)
    kakao_url = models.CharField(max_length=200)
    onOff = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    oneLine = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    board_text = RichTextUploadingField(null=True)

# 카테고리와 시킬 예정임
    category = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title