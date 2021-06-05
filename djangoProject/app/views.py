from django.shortcuts import render
from .models import MyStudy

# Create your views here.
def home_list(request):
    # 어학 스터디 모임만 가져올 수 있음
    studyInfo = MyStudy.objects.filter()
    return render(request, 'app/home_list.html', {'studyList':studyInfo})
    # info 라는 이름은 그냥 아무거나 상관없음. - model 데이터 넘겨준것뿐.

def study_list(request):
    studyInfo = MyStudy.objects.filter()
    language_study = MyStudy.objects.filter(category="어학")
    job_study = MyStudy.objects.filter(category="취업")
    school_study = MyStudy.objects.filter(category="학습")
    etc_study = MyStudy.objects.filter(category="기타")
    return render(request, 'app/study_list.html', {'studyList':studyInfo,
    'languageList':language_study,'jobList':job_study
    ,'schoolList':school_study,'etcList':etc_study})

def login(request):
    return render(request, 'app/login.html')


def join(request):
    return render(request, 'app/join.html')