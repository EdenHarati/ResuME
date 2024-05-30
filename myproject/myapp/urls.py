# myapp/urls.py
from django.urls import path
from . import views
from .views import sign_up_view


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('uploadcvfile/', views.upload_cv_file, name='upload_cv_file'),
    path('uploadjobfile/', views.upload_job_file, name='upload_job_file'),
    path('uploadsuccess/', views.upload_success, name='upload_success'),
    path('signin/', views.sign_in_view, name='sign_in'),
    path('sign-up/', sign_up_view, name='sign_up'),

]

# myapp/urls.py

