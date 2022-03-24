from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'fullstack/index.html')

def schedule(request):
    return render(request, 'fullstack/schedule.html')

def speakers(request):
    return render(request, 'fullstack/speakers.html')

def about(request):
    return render(request, 'fullstack/about.html')