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
    path('logout/', logout, name='logout'),
    # CRUD
    path('dashboard/', dashboard, name='dashboard'),
    path('create_record/', createrecord, name='create_record'),
    path('update_record/<int:pk>/', update_record, name='update_record'),
    path('view_record/<int:pk>/', view_single_record, name='view_record'),
    path('delete_record/<int:pk>/', delete_record, name='delete_record'),
    path('update_sales_order/<int:pk>/', update_sales_order, name='update_sales_order'),
    path('delete_sales_order/<int:pk>/', delete_sales_order, name='delete_sales_order'),
    # path('create_invoice/', create_invoice, name='create_invoice'),
    # urls.py
    path('create_record/create_invoice/<int:so_id>/', create_invoice, name='create_invoice'),
]
