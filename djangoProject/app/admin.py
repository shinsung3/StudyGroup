from django.contrib import admin
from .models import MyStudy, QnA1
# Register your models here.

# PK, TITLE 보여주기
class MyStudyListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
class QnA1ListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'contents')

admin.site.register(MyStudy, MyStudyListAdmin)
admin.site.register(QnA1, QnA1ListAdmin)
