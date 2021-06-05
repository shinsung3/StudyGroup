from django.contrib import admin
from .models import MyStudy, QnA
# Register your models here.

# PK, TITLE 보여주기
class MyStudyListAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')

admin.site.register(MyStudy, MyStudyListAdmin)
