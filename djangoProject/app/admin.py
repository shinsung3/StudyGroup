from django.contrib import admin
from .models import MyStudy, QnA2
# Register your models here.

# PK, TITLE 보여주기
class MyStudyListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
class QnA2ListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'contents')

admin.site.register(MyStudy, MyStudyListAdmin)
admin.site.register(QnA2, QnA2ListAdmin)
