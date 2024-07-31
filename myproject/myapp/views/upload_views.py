from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import UploadFileForm
from ..models import UploadedFile
from django.core.exceptions import PermissionDenied

class UploadCVFileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'uploadCV.html', {'form': form})
    
    def modify_cv(self, request, cv):
        request.session['current_cv'] = cv

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_instance = form.save(commit=False)
            uploaded_file_instance.user = request.user
            uploaded_file_instance.save()

            file_path = uploaded_file_instance.file.path
            with open(file_path, 'r') as file:
                current_cv = file.read()
            self.modify_cv(request, current_cv)
            return redirect('upload_job_file')
        return render(request, 'uploadCV.html', {'form': form})

class UploadJobFileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'uploadJobDescription.html', {'form': form})
    

    def modify_job_description(self, request, jd):
        request.session['role_description'] = jd

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_instance = form.save(commit=False)
            uploaded_file_instance.user = request.user
            uploaded_file_instance.save()

            file_path = uploaded_file_instance.file.path
            with open(file_path, 'r') as file:
                role_description = file.read()
            self.modify_job_description(request, role_description)
            return redirect('upload_success')
        return render(request, 'uploadJobDescription.html', {'form': form})

class UploadSuccessView(LoginRequiredMixin, View):
    def get(self, request):
        current_cv = request.session.get('current_cv', 'Initial CV')
        role_description = request.session.get('role_description', 'Initial Job Description')
        result = None # generate_cv(current_cv, role_description, " sk-")
        result_with_new_lines = None # result.replace('. ', '.\n')
        return render(request, 'upload_success.html', {'result': result_with_new_lines})
