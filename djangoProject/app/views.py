from django.shortcuts import render
from .models import MyStudy

# Create your views here.
def home_list(request):
    studyInfo = MyStudy.objects.filter()
    print(studyInfo)
    return render(request, 'app/home_list.html', {'info':studyInfo})
    # info 라는 이름은 그냥 아무거나 상관없음. - model 데이터 넘겨준것뿐.