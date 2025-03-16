"""
URL configuration for sales_purchase_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sales.views import * 
# home, sales_order_list, sales_order_create, sales_order_detail  # Import directly from sales
from purchases.views import purchase_order_list, purchase_order_create, purchase_order_detail  # Import directly from purchases
from inventory.views import product_list, product_create, product_detail  # Import directly from inventory

urlpatterns = [
    path('', home, name='home'),
    path('sales/', sales_order_list, name='sales_order_list'),
    path('create/', sales_order_create, name='sales_order_create'),
    path('<int:pk>/', sales_order_detail, name='sales_order_detail'),
    path('admin/', admin.site.urls),
    path('purchases/', include('purchases.urls')),
    path('accounts/', include('accounts.urls')),
    path('inventory/', include('inventory.urls')),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]