from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Привет Андрей')

def profile(request):
    return render(request, 'home.html')


# Create your views here.
