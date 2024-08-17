# # myapp/urls.py
# from django.urls import path
# from . import views

from django.urls import path
from .views.auth_views import SignUpView, SignInView, SignOutView
from .views.upload_views import UploadCVFileView, UploadJobFileView, UploadSuccessView,SaveGeneratedCVView, ChoosingMainFlow
from .views.user_views import ViewUserCVView, ViewUsernamesView
from .views.general_views import AboutView, HomepageView
from .views.questionnaire import QuestionnaireView

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
    path('choose-main-flow/', ChoosingMainFlow.as_view(), name='choose_main_flow'),
    path('new-cv-flow/', QuestionnaireView.as_view(), name='start_questionnaire'),
    path('save_generated_cv/', SaveGeneratedCVView.as_view(), name='save_generated_cv'),
]


