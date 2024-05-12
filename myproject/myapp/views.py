
# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render
# from .forms import CVForm TODO
from .utils import generate_cv


def index(request):
    return HttpResponse("Hello, world! This is a demo Django app.")

def about(request):
    return HttpResponse("This is the about page.")

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
