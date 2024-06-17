from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from ..models import UploadedFile

class ViewUserCVView(LoginRequiredMixin, View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        if request.user != user and not request.user.is_staff:
            raise PermissionDenied
        uploaded_file = get_object_or_404(UploadedFile, user=user)
        file_path = uploaded_file.file.path
        with open(file_path, 'r') as file:
            user_cv = file.read()
        return render(request, 'view_user_cv.html', {'user_cv': user_cv, 'user': user})

class ViewUsernamesView(View):
    def get(self, request):
        users = User.objects.all()
        usernames = [user.username for user in users]
        return render(request, 'usernames.html', {'usernames': usernames})
