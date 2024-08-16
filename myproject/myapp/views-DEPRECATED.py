# myapp/views-DEPRECATED.py
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SignInForm, SignUpForm, UploadFileForm
from .utils import generate_cv
from .models import UploadedFile
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

current_cv = "Initial CV"
role_description = "Initial Job Description"



def about(request):
    return HttpResponse("This is the about page.")

def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'registration_success.html', {'user': user})
    else:
        form = SignUpForm()
    return render(request, 'login/sign_up.html', {'form': form})

def sign_in_view(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('upload_job_file')
    else:
        form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})

@login_required
def upload_cv_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_instance = form.save(commit=False)
            uploaded_file_instance.user = request.user
            uploaded_file_instance.save()

            file_path = uploaded_file_instance.file.path
            with open(file_path, 'r') as file:
                current_cv = file.read()
            modify_cv(request, current_cv)
            return redirect('upload_job_file')
    else:
        form = UploadFileForm()
    return render(request, 'uploadCV.html', {'form': form})

@login_required
def upload_job_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_instance = form.save(commit=False)
            uploaded_file_instance.user = request.user
            uploaded_file_instance.save()

            file_path = uploaded_file_instance.file.path
            with open(file_path, 'r') as file:
                role_description = file.read()
            modify_job_description(request, role_description)
            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'uploadJobDescription.html', {'form': form})

@login_required
def upload_success(request):
    current_cv = request.session.get('current_cv', 'Initial CV')
    role_description = request.session.get('role_description', 'Initial Job Description')
    result =None #generate_cv(current_cv, role_description, " sk-")
    result_with_new_lines = None#result.replace('. ', '.\n')
    return render(request, 'upload_success.html', {'result': result_with_new_lines})

@login_required
def view_user_cv(request, username):
    user = get_object_or_404(User, username=username)
    if request.user != user and not request.user.is_staff:
        raise PermissionDenied
    uploaded_file = get_object_or_404(UploadedFile, user=user)
    file_path = uploaded_file.file.path
    with open(file_path, 'r') as file:
        user_cv = file.read()
    return render(request, 'view_user_cv.html', {'user_cv': user_cv, 'user': user})

def modify_cv(request, cv):
    request.session['current_cv'] = cv

def modify_job_description(request, jd):
    request.session['role_description'] = jd

def view_usernames(request):
    # Retrieve all user objects
    users = User.objects.all()

    # Extract usernames from user objects
    usernames = [user.username for user in users]

    # Render the usernames in a template or return them as a response
    return render(request, 'usernames.html', {'usernames': usernames})

def homepage(request):
    return render(request, 'index.html')