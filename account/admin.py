from django.contrib import admin
from .models import Account
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# Register your models here.
class UserCreationFrom(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ('email', 'contact_no')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password doesnot match')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('email', 'password', 'contact_no', 'is_active', 'is_admin',)

    def clean_password(self):
        return self.initial['password']


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationFrom
    list_display = ('email', 'contact_no', 'is_admin', 'is_active')
    list_filter = ('is_admin', 'is_active')
    search_fields = ('email',)
    # fieldsets = (
    #     (None, {'fields': ('email', 'password',)}),
    #     ('Personal info', {'fields': ('contact_no',)}),
    #     ('Permission', {'fields': ('is_admin', 'is_active')}),
    # )
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'contact_no', 'is_admin', 'is_active'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'contact_no', 'password1', 'password2', 'is_admin', 'is_active'),
        }),
    )

    filter_horizontal = []
    ordering = ('-email',)
    # list_display_links =
    # list_editable = ('email', 'contact_no', 'is_admin',)
    # list_per_page = 1


admin.site.register(Account, UserAdmin)
