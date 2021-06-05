from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home_list, name='home_list'),
    path('study_list/', views.study_list, name='study_list'),
    path('login/', views.login, name='login'),
    path('login/join/', views.join, name='join'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
]