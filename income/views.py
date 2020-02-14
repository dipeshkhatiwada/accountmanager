from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from .forms import IncomeCateogyForm, IncomeFrom
from .models import IncomeCategory, Income


# Create your views here.
class IncomeCategoryView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'income_category.html'

    def get(self, request):
        context = {
            'form': IncomeCateogyForm(),
            'categories': IncomeCategory.objects.filter(user_id=request.user.id)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = IncomeCateogyForm(request.POST)
        if forms.is_valid():
            data = forms.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request, messages.SUCCESS, "Category saved successfully")
            return redirect('income')
        else:
            messages.add_message(request, messages.ERROR, "Category saved error")
            return redirect('income_category')


class IncomeAddView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'add_income.html'

    def get(self, request):
        context = {
            'form': IncomeFrom(request.user.id)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = IncomeFrom(request.user.id, request.POST, request.FILES or None)
        if forms.is_valid():
            data = forms.save()

            messages.add_message(request, messages.SUCCESS, "Income saved successfully")
            return redirect('income')
        else:
            messages.add_message(request, messages.ERROR, "Income saved error")
            return redirect('income_category')


class IncomeView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'income.html'

    def get(self, request):
        context = {
            'incomes': Income.objects.filter(
                category__in=IncomeCategory.objects.filter(user_id=request.user.id)).order_by('-date')
        }
        return render(request, self.template_name, context)


class IncomeEditView(LoginRequiredMixin, UpdateView):
    login_url = '/account/login'
    template_name = 'edit_income.html'
    form = IncomeFrom
    fields = ['title', 'description', 'price', 'image', 'category']
    success_url = reverse_lazy('income')

    def get_context_data(self, **kwargs):
        context = super(IncomeEditView, self).get_context_data()
        context['form'] = IncomeFrom(self.request.user.id, instance=Income.objects.get(slug=self.kwargs['slug']))
        return context

    def get_object(self, queryset=None):
        queryset = Income.objects.filter(slug=self.kwargs['slug'])
        return super(IncomeEditView, self).get_object(queryset)


class IncomeDeleteView(LoginRequiredMixin, View):
    login_url = '/account/login'
    template_name = 'edit_income.html'

    def get(self, request, id):
        income = Income.objects.get(pk=id)
        income.delete()
        messages.add_message(request, messages.SUCCESS, "Income successfully deleted")
        return redirect('income')
