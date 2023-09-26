from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .models import *
from .forms import *
# Create your views here.

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'invalid username or password')
    else:
        return  render(request,'auth/login.html')
    
def home(request):
    return render(request, 'dashboard/home.html')

def signout(request):
    logout(request)
    return redirect('/login')

def product(request):
    if request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    else:
        
     return render(request, 'dashboard/products/index.html')
 
def category(request):
    if request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    else:
        
     return render(request, 'dashboard/categories/index.html')
 
def customer(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        
        customer = Customer(name=name,phone=phone,address=address)
        customer.save()
        print(customer)
    elif request.method == 'PUT':
        pass
    else:
     customer = Customer.objects.all()
     print(customer)
     form = CustomerForm()
     context = {
        'customer':customer,
         'form':form
     }
     return render(request, 'dashboard/customer/index.html',context)
 
def prduct_order(request):
    if request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    else:
        
     return render(request, 'dashboard/orders/index.html')
