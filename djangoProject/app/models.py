from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class MyStudy(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200)
    totalMember = models.IntegerField(null=True)
    kakao_url = models.CharField(max_length=200)
    onOff = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200, null=True)
    oneLine = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    study_duration = models.CharField(max_length=200, null=True)
    board_text = RichTextUploadingField(null=True)
    count = models.IntegerField(null=True)
    is_finish = models.CharField(max_length=200, null=True)

# 카테고리와 시킬 예정임
    category = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class QnA(models.Model):
    study = models.ForeignKey(MyStudy, on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    writer = models.CharField(max_length=500)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class QnA1(models.Model):
    study = models.ForeignKey(MyStudy, on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    writer = models.CharField(max_length=500)

    def publish(self):
        self.save()

    def __str__(self):
        return self.contents