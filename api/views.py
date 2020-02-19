from rest_framework import mixins
from rest_framework import generics
from .serializer import IncomeCategorySerializer, IncomeSerializer
from income.models import IncomeCategory,Income

class IncomeCategoryView(mixins.ListModelMixin,generics.GenericAPIView):
    serializer_class = IncomeCategorySerializer
    queryset = IncomeCategory.objects.all()

    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)
class IncomeView(mixins.ListModelMixin,generics.GenericAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()

    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)