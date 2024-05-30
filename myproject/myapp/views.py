from audioop import reverse

# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render
# from .forms import CVForm TODO
from .utils import generate_cv
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .utils import generate_cv
# global current_cv
# global role_description

current_cv = "Initial CV"
role_description = "Initial Job Description"


def index(request):
    return HttpResponse("Hello, world! This is a demo Django app.")

def about(request):
    return HttpResponse("This is the about page.")

def upload_job_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
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
        form = UploadFileForm()
    return render(request, 'uploadJobDescription.html', {'form': form})

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
    result = generate_cv(current_cv, role_description, "sk-")
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
