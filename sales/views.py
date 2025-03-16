from os import name
from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm, SalesOrderForm, UserCreationForm, LoginForms
# Create your views here.

# View to list all sales orders
def home(request):
    return render(request, 'nav_base/home.html')

# Register
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('',)
    context = {'form':form}
    return render(request, 'user/register.html', context=context)

def login(request):
    return render(request, 'user/login.html')

def sales_order_list(request):
    sales_orders = SalesOrder.objects.all()
    for order in sales_orders:
        order.total_amount = order.qty * order.rate  # Calculate total amount
    return render(request, 'sales/sales_order_list.html', {'sales_orders' : sales_orders})

# View to create a new sales order
def sales_order_create(request):
    if request.method == 'POST':
        form = SalesOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_order_list')  # Redirect to the list view after saving
    else:
        form = SalesOrderForm()
    return render(request, 'sales/sales_order_form.html', {'form': form})

# View to detail a specific sales order
def sales_order_detail(request, pk):
    sales_order = SalesOrder.objects.get(pk=pk)
    return render(request, 'sales/sales_order_detail.html', {'sales_order': sales_order})