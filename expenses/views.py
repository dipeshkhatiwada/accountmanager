from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import ExpensesCategoryForm,ExpensesForm
# Create your views here.
class ExpenesCategoryView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'expenses_category.html'

    def get(self,request):
        context = {
            'form':ExpensesCategoryForm()
        }
        return render(request,self.template_name, context)
    def post(self, request, *args, **kwargs):
        forms = ExpensesCategoryForm(request.POST)
        if forms.is_valid():
            data = forms.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request, messages.SUCCESS, "Category saved successfully")
            return redirect('expenses')
        else:
            messages.add_message(request, messages.ERROR, "Category saved error")
            return redirect('expenses_category')



class ExpensesAddView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'add_expenses.html'
    def get(self,request):
        context = {
            'form': ExpensesForm()
        }
        return render(request,self.template_name,context)
    def post(self, request, *args, **kwargs):
        forms = ExpensesForm(request.POST, request.FILES or None)
        if forms.is_valid():
            data = forms.save()

            messages.add_message(request, messages.SUCCESS, "Expenses saved successfully")
            return redirect('expenses')
        else:
            messages.add_message(request, messages.ERROR, "Expenses saved error")
            return redirect('expenses_category')

class ExpenseView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'expenses.html'

    def get(self,request):
        return render(request,self.template_name)