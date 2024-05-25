# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('uploadfile/', views.upload_file, name='upload_file'),
    path('uploadsuccess/', views.upload_file, name='upload_success'),
]
