from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# View to list all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

# View to create a new product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the list view after saving
    else:
        form = ProductForm()
    return render(request, 'inventory/product_form.html', {'form': form})

# View to detail a specific product
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'inventory/product_detail.html', {'product': product})

# View for inventory
def inventory(request):
    return render(request, 'inventory/inventory.html')  # Create this template
# Create your views here.
