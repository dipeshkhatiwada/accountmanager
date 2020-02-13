from .models import Expenses,ExpensesCategory
from django import forms
from account.models import Account
from .models import ExpensesCategory
class ExpensesCategoryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Category Title'}))

    class Meta:
        model = ExpensesCategory
        fields = ['title', ]


class ExpensesForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=None)

    def __init__(self,id,*args,**kwargs):
        super(ExpensesForm, self).__init__(*args,**kwargs)
        self.fields['category'].queryset=ExpensesCategory.objects.filter(user_id=id)
    class Meta:
        model = Expenses
        fields ='__all__'