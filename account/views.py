from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import *

def home(request):
      orders = Order.objects.all()
      customers = Customer.objects.all()
      total_customers = customers.count()
      total_orders = orders.count()
      delivered = orders.filter(status='Delivered').count()
      pending = orders.filter(status='pending').count()


    #   context = {'orders':orders, 'customers': customers, 'total_customers':total_customers,'total_orders'= total_orders }
      context = {'orders':orders, 'customers': customers,
       'total_customers':total_customers, 'total_orders': total_orders,
        'delivered':delivered, 'pending':pending}


      return render(request,'account/deshboard.html' ,context)

def products(request):
    products = Products.objects.all()
    return render(request, 'account/products.html', {'products': products})

def customers(request,pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    context = {'customer': customer, 'orders':orders}
    return render(request,'account/customers.html', context)