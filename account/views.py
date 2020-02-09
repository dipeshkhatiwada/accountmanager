from django.contrib.auth import logout
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404


# Create your views here.
def signup(request):
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'login.html')


def password_forgot(request):
    return render(request, 'password_forgot.html')


def signout(request):
    logout(request)
    return redirect('signin')


def dashboard(request):
    return render(request, 'dashboard.html')
