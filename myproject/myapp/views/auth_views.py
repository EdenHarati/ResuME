from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import SignInForm, SignUpForm

sign_up_page = 'auth/sign_up.html'
sign_in_page = 'auth/sign_in.html'

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, sign_up_page, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'registration_success.html', {'user': user})
        return render(request, sign_up_page, {'form': form})

class SignInView(View):
    def get(self, request):
        form = SignInForm()
        return render(request,sign_in_page, {'form': form})

    def post(self, request):
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('upload_job_file')
        return render(request, sign_in_page, {'form': form})


class SignOutView(View):
    def get(self, request):
        logout(request)
        return redirect('sign_in')
