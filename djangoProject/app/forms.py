from django import forms
from django.db.models import fields
from .models import MyStudy

class StudyForm(forms.ModelForm):
    class Meta:
        model = MyStudy
        fields = (
            'title',
            'contents',
            'region',
            'totalMember',
            'kakao_url',
            'onOff',
            'img_url',
            'oneLine',
            'duration',
            'study_duration',
            'board_text',
            'count',
            'is_finish',
            'category',
            )