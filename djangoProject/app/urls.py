from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),
    path('study_list/', views.study_list, name='study_list'),
    path('login/', views.login, name='login'),
    path('login/join/', views.join, name='join'),
    # path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
]