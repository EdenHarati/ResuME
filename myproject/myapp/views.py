# myapp/views.py
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import SignInForm
from .forms import SignUpForm
# from .forms import CVForm TODO
from .forms import UploadFileForm
from .utils import generate_cv
from .models import UploadedFile


# global current_cv
# global role_description

current_cv = "Initial CV"
role_description = "Initial Job Description"


# myapp/views.py






def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'registration_success.html', {'user': user})  # Render a success page
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def index(request):
    return HttpResponse("Hello, world! This is a demo Django app.")

def about(request):
    return HttpResponse("This is the about page.")

# def upload_job_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_file_instance = form.save()
#
#             # Reading the file content
#             file_path = uploaded_file_instance.file.path
#             with open(file_path, 'r') as file:
#                 role_description = file.read()
#                 modify_job_description(role_description)
#
#             # Pass the file content to the utility function
#             return redirect('upload_success')
#             # return redirect('upload_success', current_cv=current_cv, role_description='Your Role Description')
#
#
#     else:
#         form = UploadFileForm()
#     return render(request, 'uploadJobDescription.html', {'form': form})

@login_required
def upload_job_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_instance = form.save(commit=False)
            uploaded_file_instance.user = request.user
            uploaded_file_instance.file_type = 'JD'


            role_description = uploaded_file_instance.file.read().decode('utf-8')
            request.session['role_description'] = role_description

            uploaded_file_instance.save()

            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'uploadJobDescription.html', {'form': form})
#
# def upload_cv_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_file_instance = form.save()
#
#             # Reading the file content
#             file_path = uploaded_file_instance.file.path
#             with open(file_path, 'r') as file:
#                  current_cv = file.read()
#             modify_cv(current_cv)
#
#             # Pass the file content to the utility function
#             return redirect('upload_job_file')
#
#     else:
#         form = UploadFileForm()
#     return render(request, 'uploadCV.html', {'form': form})

@login_required
def upload_cv_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_instance = form.save(commit=False)
            uploaded_file_instance.user = request.user
            uploaded_file_instance.file_type = 'CV'

            # Read the file content before saving
            file = request.FILES['file']
            current_cv = file.read().decode('utf-8')
            request.session['current_cv'] = current_cv

            # Now save the instance to the database
            uploaded_file_instance.save()
    else:
        form = UploadFileForm()
    return render(request, 'uploadCV.html', {'form': form})

# def upload_success(request):
#     result = generate_cv(current_cv, role_description, " sk-")
#     result_with_new_lines = result.replace('. ', '.\n')
#     return render(request, 'upload_success.html', {'result': result_with_new_lines})
#
#     # return render(request, 'upload_success.html', {'result': result})
#     # return render(request, 'upload_success.html')

@login_required
def upload_job_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_instance = form.save(commit=False)
            uploaded_file_instance.user = request.user
            uploaded_file_instance.file_type = 'JD'
            uploaded_file_instance.save()

            role_description = uploaded_file_instance.file.read().decode('utf-8')
            request.session['role_description'] = role_description
            return redirect('upload_success')
    else:
        form = UploadFileForm()
    return render(request, 'uploadJobDescription.html', {'form': form})

@login_required
def upload_success(request):
    current_cv = request.session.get('current_cv', '')
    role_description = request.session.get('role_description', '')
    result = generate_cv(current_cv, role_description, " sk-")
    result_with_new_lines = result.replace('. ', '.\n')
    return render(request, 'upload_success.html', {'result': result_with_new_lines})

def sign_in_view(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('upload_cv_file')  # Redirect to upload CV page after sign in
    else:
        form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})
