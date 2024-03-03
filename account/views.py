from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from .models import *
from .forms import OrderForm


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


def cereatOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        # print('printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'account/order_form.html', context)    


def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance =order)
    
    if request.method == 'POST':
        # print('printing POST:', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    context = {'form':form}
    return render(request, 'account/order_form.html', context)      

def deleteOrder(request,pk):
 
    order = Order.objects.get(id=pk)  
    if request.method =="POST":
        order.delete()
        return redirect('/')      
    context = {'item':order}
    return render(request, 'account/delete.html', context)      
