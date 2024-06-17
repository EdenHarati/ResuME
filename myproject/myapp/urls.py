# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('uploadcvfile/', views.upload_cv_file, name='upload_cv_file'),
    path('uploadjobfile/', views.upload_job_file, name='upload_job_file'),
    path('uploadsuccess/', views.upload_success, name='upload_success'),
    path('sign-in/', views.sign_in_view, name='sign_in'),
    path('sign-up/', views.sign_up_view, name='sign_up'),
    path('user/<str:username>/cv/', views.view_user_cv, name='view_user_cv'),
    path('usernames/', views.view_usernames, name='usernames'),
    path('', views.homepage, name='homepage'),

]
