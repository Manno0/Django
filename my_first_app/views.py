from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Home Page!")

def not_found(request):
    return HttpResponse("Not found")

from django.shortcuts import render

# Create your views here.
