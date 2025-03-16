from django.shortcuts import render, redirect
from .models import PurchaseOrder
from .forms import PurchaseOrderForm

# View to list all purchase orders
def purchase_order_list(request):
    purchase_orders = PurchaseOrder.objects.all()
    return render(request, 'purchases/purchase_order_list.html', {'purchase_orders': purchase_orders})

# View to create a new purchase order
def purchase_order_create(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_order_list')  # Redirect to the list view after saving
    else:
        form = PurchaseOrderForm()
    return render(request, 'purchases/purchase_order_form.html', {'form': form})

# View to detail a specific purchase order
def purchase_order_detail(request, pk):
    purchase_order = PurchaseOrder.objects.get(pk=pk)
    return render(request, 'purchases/purchase_order_detail.html', {'purchase_order': purchase_order})

# Create your views here.
