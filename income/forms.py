from .models import Income, IncomeCategory
from django import forms


class IncomeCateogyForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Category Title'}))

    class Meta:
        model = IncomeCategory
        fields = ['title', ]


class IncomeFrom(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Title'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control','placeholder':'Enter Price'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Description'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=IncomeCategory.objects.all())
    class Meta:
        model = Income
        fields = '__all__'
