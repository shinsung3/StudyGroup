from django.shortcuts import get_object_or_404, redirect, render
from .models import MyStudy, QnA1
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import StudyForm

# SMTP 관련 인증
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
# from django.core.mail import EmailMessage
# from django.utils.encoding import force_bytes, force_text
# from .tokens import account_activation_token

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

    if request.method == "POST":
        id = request.POST["email"]
        pw = request.POST["pwd"]
        user = auth.authenticate(request, username=id, password=pw)

        if user is None:
            message = "아이디가 또는 비밀번호가 틀렸습니다."
            return render(request, 'app/login.html',{"messageID":message})
        else:
            auth.login(request, user)
            return redirect("/")
    return render(request, 'app/login.html')


def join(request):

    nameCheck = User.objects.filter()
    print("join 실행")
    if request.method== 'POST': #form이 post로 던지면 여기서 처리
        print("여기는 포스트 요청")
        email = request.POST['email']
        name = request.POST['name']
        pwd = request.POST['pwd']
        # print(name)
        # print(email)
        # print(pwd)
        c = 0
        for name1 in nameCheck:
            print(name1.first_name)
            if name1.first_name==name:
                c = 1
        if c!=1:
            User.objects.create_user(username=email, password=pwd, first_name=name)
            return redirect("/")
        else :
            return render(request, 'app/join.html', {'nameCompare1':"이미 존재하는 닉네임입니다"})
        # user.is_active = False # 유저 비활성화
        # user.save()
        # current_site = get_current_site(request)
        # message = render_to_string('app/activation_email.html', {
        #     'user': user,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token': account_activation_token.make_token(user),
        # })
        # mail_title = "계정 활성화 확인 이메일"
        # mail_to = email
        # email = EmailMessage(mail_title, message, to=[mail_to])
        # email.send()
    else:
        print("join 마지막")
        return render(request, 'app/join.html')

# # 계정 활성화 함수(토큰을 통해 인증)
# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         auth.login(request, user)
#         return redirect("/")
#     else:
#         return render(request, 'app/join.html')
#     return

def logout(request):
    auth.logout(request)
    return redirect("/")

def study_list_detail(request, pk):
    studyDetail = get_object_or_404(MyStudy, pk=pk) #데이터 받아오기
    contents = QnA1.objects.filter(study=studyDetail)
    auth.authenticate()
    if request.method == 'POST':
        writer = request.POST['writer']
        content = request.POST['contents']
        QnA1.objects.create(study = studyDetail,
        writer=writer, contents=content)
        url = "/study_list/"+str(pk)
        return redirect("/study_list/"+str(pk))
    return render(request, 'app/detail.html', {'studyDetails':studyDetail,
        'contents':contents})

def updateStudy(request, pk):
    studyDetail = get_object_or_404(MyStudy, pk=pk) #데이터 받아오기
    studyDetail.count += 1
    studyDetail.save()
    print(studyDetail.count)
    url = "/study_list/"+str(pk)
    return redirect(url)

def updateFinish(request, pk):
    studyDetail = get_object_or_404(MyStudy, pk=pk) #데이터 받아오기
    studyDetail.is_finish = "종료"
    studyDetail.save()
    url = "/study_list/"+str(pk)
    return redirect(url)

def qna_remove(request, pk):
    if request.method == "POST":
        QnA1.objects.get(pk=pk).delete()
        return redirect("/study_list")

def my_page(request):
    nameCheck = User.objects.filter()
    if request.method=="POST":
        email = request.POST['email']
        name = request.POST['name']
        c = 0
        for name1 in nameCheck:
            print(name1.first_name)
            if name1.first_name==name:
                c = 1
        if c!=1:
            User.objects.update(first_name=name)
            return redirect("/")
        else :
            return render(request, 'app/my_page.html', {'nameCompare1':"이미 존재하는 닉네임입니다"})


    return render(request, "app/my_page.html", {'userID':nameCheck})

def search(request):
    if request.method=="POST":
        text = request.POST['text']
        studyInfo = MyStudy.objects.filter(title__contains=text)
        print(studyInfo)
        return render(request, "app/search.html", {'studySearch':studyInfo})
    return render(request, "app/search.html")

def create_study(request):
    #forms.py 이용
    if request.method=="POST":
        # study_form = StudyForm()
        title = request.POST['title']
        region = request.POST['region']
        totalMember = request.POST['totalMember']
        kakao_url = request.POST['kakao_url']
        onOff = request.POST['onOff']
        img_url = request.POST['img_url']
        oneLine = request.POST['oneLine']
        duration = request.POST['duration']
        study_duration = request.POST['study_duration']
        count = request.POST['count']
        category = request.POST['category']
        board_text = request.POST['board_text']
        # MyStudy = study_form.save(commit=False)
        # MyStudy = study_form.board_text.save(commit=False)
        # author = request.POST['author']
        author = request.user
        MyStudy.objects.create(title = title,
        region=region,totalMember=totalMember,
        kakao_url=kakao_url,onOff=onOff,
        img_url=img_url, oneLine=oneLine,
        duration=duration, study_duration=study_duration,
        count=count, category=category,board_text=board_text,
        author = author
        )
        return redirect("/")
    return render(request, "app/my_group.html")