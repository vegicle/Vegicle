from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("User app")


def login_form(request):
    return HttpResponse("Login Form")


def signup_form(request):
    return HttpResponse("signup")
