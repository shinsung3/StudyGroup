from django.shortcuts import render
from .models import MyStudy

# Create your views here.
def home_list(request):
    # 어학 스터디 모임만 가져올 수 있음
    studyInfo = MyStudy.objects.filter(category="어학")
    return render(request, 'app/home_list.html', {'studyList':studyInfo})
    # info 라는 이름은 그냥 아무거나 상관없음. - model 데이터 넘겨준것뿐.