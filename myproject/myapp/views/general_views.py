from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class AboutView(View):
    def get(self, request):
        return HttpResponse("This is the about page.")

class HomepageView(View):
    def get(self, request):
        return render(request, 'index.html')
