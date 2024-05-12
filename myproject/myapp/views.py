
# myapp/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is a demo Django app.")

def about(request):
    return HttpResponse("This is the about page.")
