# myapp/views.py
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import SignInForm
from .forms import SignUpForm
# from .forms import CVForm TODO
from .forms import UploadFileForm
from .utils import generate_cv

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
            return render(request, 'registration_success.html', {'user': user})
    else:
        form = SignUpForm()
    return render(request, 'login/sign_up.html', {'form': form})


def index(request):
    return HttpResponse("Hello, world! This is a demo Django app.")

def about(request):
    return HttpResponse("This is the about page.")

def upload_job_file(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            uploaded_file_instance = form.save()

            # Reading the file content
            file_path = uploaded_file_instance.file.path
            with open(file_path, 'r') as file:
                role_description = file.read()
                modify_job_description(role_description)

            # Pass the file content to the utility function
            return redirect('upload_success')
            # return redirect('upload_success', current_cv=current_cv, role_description='Your Role Description')


    else:
        form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})

def upload_cv_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_instance = form.save()

            # Reading the file content
            file_path = uploaded_file_instance.file.path
            with open(file_path, 'r') as file:
                 current_cv = file.read()
            modify_cv(current_cv)

            # Pass the file content to the utility function
            return redirect('upload_job_file')
    else:
        form = UploadFileForm()
    return render(request, 'uploadCV.html', {'form': form})

def upload_success(request):
    result = generate_cv(current_cv, role_description, " sk-")
    result_with_new_lines = result.replace('. ', '.\n')
    return render(request, 'upload_success.html', {'result': result_with_new_lines})

    # return render(request, 'upload_success.html', {'result': result})
    # return render(request, 'upload_success.html')

def modify_cv(cv):
    global current_cv
    current_cv = cv


def modify_job_description(jd):
    global role_description
    role_description = jd
# TODO
# def generate_cv_view(request):
#     if request.method == 'POST':
#         form = CVForm(request.POST, request.FILES)
#         if form.is_valid():
#             current_cv = form.cleaned_data['current_cv'].read().decode('utf-8')
#             role_description = form.cleaned_data['role_description']
#             api_key = 'your-api-key'  # Replace 'your-api-key' with your actual OpenAI API key
#             generated_cv = generate_cv(current_cv, role_description, api_key)
#             # Save generated_cv to database or display it in the template
#             return render(request, 'generated_cv.html', {'generated_cv': generated_cv})
#     else:
#         form = CVForm()
#     return render(request, 'generate_cv.html', {'form': form})







# myapp/views.py


def sign_in_view(request):
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('upload_job_file')  # Redirect to a success page
    else:
        form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})
