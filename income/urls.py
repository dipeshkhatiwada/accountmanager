from django.urls import  path
from .views import IncomeCategoryView,IncomeAddView,IncomeView, IncomeEditView, IncomeDeleteView
urlpatterns = [
    path('category/',IncomeCategoryView.as_view(),name='income_category'),
    path('create/',IncomeAddView.as_view(),name='income_add'),
    path('',IncomeView.as_view(),name='income'),
    path('edit/<slug:slug>', IncomeEditView.as_view(), name='income_edit'),
    path('delete/<slug:slug>', IncomeDeleteView.as_view(), name='income_delete'),
]