# # myapp/urls.py
# from django.urls import path
# from . import views

from django.urls import path
from .views.auth_views import SignUpView, SignInView, SignOutView
from .views.upload_views import UploadCVFileView, UploadJobFileView, UploadSuccessView
from .views.user_views import ViewUserCVView, ViewUsernamesView
from .views.general_views import AboutView, HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('sign_out/', SignOutView.as_view(), name='sign_out'),
    path('upload-cv/', UploadCVFileView.as_view(), name='upload_cv_file'),
    path('upload-job/', UploadJobFileView.as_view(), name='upload_job_file'),
    path('upload-success/', UploadSuccessView.as_view(), name='upload_success'),
    path('view-cv/<str:username>/', ViewUserCVView.as_view(), name='view_user_cv'),
    path('usernames/', ViewUsernamesView.as_view(), name='view_usernames'),
]


# urlpatterns = [
#     path('about/', views.about, name='about'),
#     path('uploadcvfile/', views.upload_cv_file, name='upload_cv_file'),
#     path('uploadjobfile/', views.upload_job_file, name='upload_job_file'),
#     path('uploadsuccess/', views.upload_success, name='upload_success'),
#     path('sign-in/', views.sign_in_view, name='sign_in'),
#     path('sign-up/', views.sign_up_view, name='sign_up'),
#     path('user/<str:username>/cv/', views.view_user_cv, name='view_user_cv'),
#     path('usernames/', views.view_usernames, name='usernames'),
#     path('', views.homepage, name='homepage'),

# ]
