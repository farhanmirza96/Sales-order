from os import name
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import CreateUserForm, SalesOrderForm, UserCreationForm, LoginForms, AddRecordForm, UpdateRecordForm, UpdateSalesOrder
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants as DEFAULT_MESSAGE_LEVELS
from datetime import datetime
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
            # messages.success(request, 'Account created successfully')
            # return redirect('',)
    context = {'form':form}
    return render(request, 'user/register.html', context=context)

# login user 

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
            return redirect('home')
    context = {'form':form}
    return render(request, 'user/login.html', context=context)

# dashboard
@login_required(login_url='login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    return render(request, 'nav_base/dashboard.html', context=context)

@login_required(login_url='login')
def createrecord(request):
    form = AddRecordForm()
    if request.method == 'POST':
        form = AddRecordForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Record created successfully')
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'nav_base/create_record.html', context = context)

@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            # messages.add_message(request, DEFAULT_MESSAGE_LEVELS.SUCCESS, 'Record updated successfully')
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'nav_base/update_record.html', context = context)

# read or view single record
@login_required(login_url='login')
def view_single_record(request, pk):
    all_records = Record.objects.get(id=pk)
    context = {'record': all_records}
    return render(request, 'nav_base/view_record.html', context = context)

# delete record
@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    # messages.success(request, 'Record deleted successfully')
    return redirect('dashboard')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


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
    context = {'form': form}
    return render(request, 'sales/sales_order_form.html', context)

# View to detail a specific sales order
def sales_order_detail(request, pk):
    sales_order = SalesOrder.objects.get(pk=pk)
    invoices = Invoice.objects.filter(sales_order=sales_order).order_by('-invoice_date')
    return render(request, 'sales/sales_order_detail.html', {'sales_order': sales_order, 'invoices': invoices})

@login_required(login_url='login')
def update_sales_order(request, pk):
    sales_order = SalesOrder.objects.get(id=pk)
    form = UpdateSalesOrder(instance=sales_order)
    if request.method == 'POST':
        form = UpdateSalesOrder(request.POST, instance=sales_order)
        if form.is_valid():
            form.save()
            # messages.add_message(request, DEFAULT_MESSAGE_LEVELS.SUCCESS, 'Record updated successfully')
            return redirect('sales_order_list')
    context = {'form': form}
    return render(request, 'sales/update_sales_order.html', context = context)

# delete sales order
@login_required(login_url='login')
def delete_sales_order(request, pk):
    sales_order = SalesOrder.objects.get(id=pk)
    sales_order.delete()
    # messages.success(request, 'Sales order deleted successfully')
    return redirect('sales_order_list')

@login_required(login_url='login')
def create_invoice(request, so_id):
    try:
        sales_order = SalesOrder.objects.get(pk=so_id)
    except SalesOrder.DoesNotExist:
        messages.error(request, 'Sales order not found')
        return redirect('sales_order_list')

    # Check if sales order is completed
    if sales_order.status == 'Completed':
        messages.error(request, 'Cannot create invoice for completed sales order')
        return redirect('sales_order_detail', sales_order_id=so_id)
    
    if request.method == 'POST':
        invoice_qty = int(request.POST.get('invoice_qty', 0))
        
        if invoice_qty > sales_order.qty:
            messages.error(request, 'Invoice quantity cannot exceed remaining quantity')
            return redirect('sales_order_detail', pk=sales_order_id)
        
        # Create new invoice
        invoice = Invoice.objects.create(
            sales_order=sales_order,
            invoice_number=f'INV-{sales_order.id}-{datetime.now().strftime("%Y%m%d-%H%M%S")}',
            invoice_date=datetime.now(),
            invoice_qty=invoice_qty,
            invoice_rate=sales_order.rate,
            invoice_total_amount=invoice_qty * sales_order.rate
        )
        
        # Update remaining quantity
        if sales_order.invoiced_qty >= sales_order.qty:
            sales_order.status = 'completed'
        sales_order.invoiced_qty += invoice_qty
        sales_order.remaining_qty = sales_order.qty - sales_order.invoiced_qty
        sales_order.save()
        
        messages.success(request, f'Invoice created successfully. Remaining quantity: {sales_order.qty}')
        return redirect('sales_order_list')
    
    context = {
        'sales_order': sales_order,
        'max_qty': sales_order.qty
    }
    return render(request, 'sales/invoice_form.html', context)

@login_required(login_url='login')
def completed_so(request):
    completed_orders = SalesOrder.objects.filter(status='Completed').order_by('-id')
    return render(request, 'sales/completed_so.html', {'completed_orders': completed_orders})