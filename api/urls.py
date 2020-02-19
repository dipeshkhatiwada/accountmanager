from django.urls import  path
from .views import IncomeCategoryView,IncomeView
urlpatterns = [
    path('income-category/',IncomeCategoryView.as_view(),name='income-category'),
    path('income/',IncomeView.as_view(),name='income'),

]