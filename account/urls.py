from django.urls import path
from .views import Login, Register, ForgotPassword, Dashboard, Signout
from . import views
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('password-forgot/', ForgotPassword.as_view(), name='password_forgot'),
    path('logout/', Signout.as_view(), name='signout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

]