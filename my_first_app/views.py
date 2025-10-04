from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

    


def home(request):
    return HttpResponse("Welcome to the Home Page!")

def not_found(request):
    return HttpResponse("Not found")

class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page!")

class NotFoundView(View):
    def get(self, request):
        return HttpResponse("404 Not Found")