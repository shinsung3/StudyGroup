# StudyGroup
StudyGroup



- 흐름: 로그인한 회원이 [Home]과 [study]페이지 하단 우측에 [스터디 생성하기]버튼을 클릭하면 작성 팝업?창이 뜬다. 
- 0. [스터디 생성하기]버튼 클릭시 로그인 여부확인을 하고, 로그인 되어있는 회원일 시 작성권한부여, 비회원일시 회원가입 페이지로 이동한다. 
  1. [사진]:[home]과[study],[my group]의 스터디목록에서 보여짐, [카테고리]설정, [제목], [스터디기간],[지역],[모집인원]:현재참여신청인원/총모집인원표시,[온·오프라인] :온라인 or 오프라인 , [모집기간],[카카오톡오픈채팅] :입력전 'default로 회색 글씨로 카카오톡에서 오픈채팅방 생성 후 링크를 복사하여 적어주세요'라고 적혀있음, [한줄소개글]: 스터디 목록에서 보이는 한줄소개  
  2. 1-1 [카테고리]는 [어학],[취업],[학습],[기타]로 이루어짐 
  3. [스터디 소개]: 어떤/무슨 스터디인지 작성자가 소개하는 글을 작성할 수 있음 3.[스터디 방식]: 작성자가 스터디 방식 소개글을 작성할 수 있음 
  4. []내용 모두 필수로 작성해야됨. 5. 하단 중앙에 [생성하기] 버튼 클릭 시 스터디가 생성됨. ->생성하기 버튼 클릭시 [study]페이지로 전환됨. [home]과[study]페이지에서 작성한 스터디가 목록에 있는걸 확인가능





### 2

- data를 views에서 전달할 때 , `return render(request, 'app/home_list.html', {'info':studyInfo})`
  - 이후, html에서 `{{info}}`해주면 화면단에 data 확인 가능
  - ![image-20210603012222428](C:\Users\tlstj\AppData\Roaming\Typora\typora-user-images\image-20210603012222428.png)



### 3

- 게시판 형태로 수정할 수 있는 텍스트 에디터 추가할 예정
  - `pip install django-ckeditor`
  - ![image-20210603012728029](C:\Users\tlstj\AppData\Roaming\Typora\typora-user-images\image-20210603012728029.png)
  - ckeditor는 관리자 페이지에서 보드를 만들어서 입력할 수 있도록 나타내줌
  - ![image-20210603014020624](C:\Users\tlstj\AppData\Roaming\Typora\typora-user-images\image-20210603014020624.png)
  - 이미지는 어디로 저장되었을까?
  - ![image-20210603014146647](C:\Users\tlstj\AppData\Roaming\Typora\typora-user-images\image-20210603014146647.png)



### 4

- Django Query
  - 카테고리별로 분류해서 보고 싶다면 django에서 filter내부에서 하면 됨.
  - 이건 그냥 Python 문법임
  - ![image-20210603015207488](C:\Users\tlstj\AppData\Roaming\Typora\typora-user-images\image-20210603015207488.png)



### 5

- 장고 템플릿
  - 메인 페이지 꾸미기
  - nav 바 만들기 성공



### 6

- 장고 업로드
  - 전반적인 레이아웃 잡기



### 7

- 부트스트랩 이용하기
  - 부트스트랩을 이용하여 첫 화면 썸네일 제작
