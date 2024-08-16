from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import UploadFileForm, UploadCVFileForm
from ..models import UploadedFile
from django.core.exceptions import PermissionDenied
from ..utils import generate_cv
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

class UploadCVFileView(LoginRequiredMixin, View):

    def get(self, request):
        form = UploadCVFileForm(user=request.user)  # Pass user here
        return render(request, 'uploadCV.html', {'form': form})

    def modify_cv(self, request, cv_content):
        request.session['current_cv'] = cv_content

    def post(self, request):
        form = UploadCVFileForm(request.POST, request.FILES, user=request.user)  # Pass user here
        if form.is_valid():
            use_existing_cv = form.cleaned_data.get('use_existing_cv')
            if use_existing_cv:
                # Use the selected existing file
                selected_file = form.cleaned_data.get('existing_cv')
                if selected_file and selected_file.file:
                    # Read the file content directly from the file object
                    file_content = selected_file.file.read().decode()  # Decode if it's text content
                else:
                    file_content = None
            else:
                # Handle new file upload
                uploaded_file_instance = form.save(commit=False)
                uploaded_file_instance.user = request.user
                uploaded_file_instance.save()
                file_content = uploaded_file_instance.file.read().decode()  # Decode if it's text content

            if file_content:
                self.modify_cv(request, file_content)

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
        result = generate_cv(current_cv, role_description, 'sk-0')
        result_with_new_lines = result.replace('. ', '.\n')
        return render(request, 'upload_success.html',
                      {'result': result_with_new_lines, 'current_cv': current_cv, 'role_description': role_description})


class ChoosingMainFlow(View):

    def get(self, request):
        # Render the 'choose_main_flow' template when the method is GET
        return render(request, 'choose_main_flow.html')

    def post(self, request):
        # Handle the POST request
        if 'existingCV' in request.POST:
            return redirect('upload_cv_file')
        elif 'NewCV' in request.POST:
            return redirect('start_questionnaire')
        return render(request, 'choose_main_flow.html')
