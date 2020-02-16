from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View

from expenses.models import Expenses
from .models import Account
from django.contrib.auth.mixins import LoginRequiredMixin
from income.models import Income
import random

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
        # chart of income as per category
        category_income = Income.objects.getIncomeByCategory(request.user.id)
        category_list = list(category_income.keys())
        category_amount = list(category_income.values())
        dayincome = Income.objects.getCurrentDayIncome(request.user.id)
        dayexpenses = Expenses.objects.getCurrentDayExpenses(request.user.id)
        new_amt=[]
        for c_amt in category_amount:
            if c_amt == None:
                new_amt.append(0.0)
            else:
                new_amt.append(c_amt)
        # chart for no of income as per category
        counted_income = list(Income.objects.countIncomeByCategory(request.user.id).values())
        count_income = []
        for no in counted_income:
            count_income.append(no)
        print(category_amount)
        color_list = ['#4e73df', '#1cc88a', '#36b9cc','#2e59d9', '#17a673', '#2c9faf','c3145dba','#4a8bdcd1','3b7d62',]
        day_saving = 0.0
        if dayincome['price__sum'] and dayexpenses['price__sum']:
            day_saving = dayincome['price__sum'] - dayexpenses['price__sum']
        bcolor=[]
        hovercolor=[]
        for i in range(0,len(category_income)):
            bcolor.append(color_list[random.randint(0,5)])
            hovercolor.append(color_list[random.randint(0,5)])

        context = {
            'dayincome':dayincome,
            'dayexpenses': dayexpenses,
            'daysaving': day_saving,
            'category_list':category_list,
            'category_amount':new_amt,
            'bcolor':bcolor,
            'hovercolor':hovercolor,
            'count_income': count_income,

        }
        return render(request, self.template_name,context)


class Signout(View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)
