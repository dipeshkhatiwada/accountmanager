from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from .models import Account
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Login(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *arg, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.add_message(request, messages.ERROR, "email and password doesnot match")
            return redirect('login')


class Register(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *arg, **kwargs):
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            user = Account.objects.create_user(email, contact_no, first_name=f_name, last_name=l_name,
                                               password=password1)
            messages.add_message(request, messages.SUCCESS, "Register successfully login to continue!")
            return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, "Password and confirm passsword doesnot match")
            return redirect('register')


class ForgotPassword(View):
    template_name = 'password_forgot.html'

    def get(self, request):
        return render(request, self.template_name)


class Dashboard(LoginRequiredMixin,  View):

    login_url = '/account/login'
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)


class Signout(View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)
