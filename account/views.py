from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    return render(request,'account/deshboard.html')
def products(request):
    return render(request,'account/products.html')
def customers(request):
    return render(request,'account/customers.html')