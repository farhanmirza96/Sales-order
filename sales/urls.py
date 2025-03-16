from django.contrib.auth import login
from django.urls import path
from .views import * 
# sales_order_list, sales_order_create, sales_order_detail  # Import the correct views

urlpatterns = [
    path('', sales_order_list, name='sales_order_list'),  # Use the correct view for the sales list
    path('create/', sales_order_create, name='sales_order_create'),
    path('<int:pk>/', sales_order_detail, name='sales_order_detail'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
