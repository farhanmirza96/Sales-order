from django.urls import path
from . import views
from .views import purchase_order_list, purchase_order_create, purchase_order_detail  # Import the views

urlpatterns = [
    path('home/', purchase_order_list, name='purchase_order_list'),
    path('', purchase_order_list, name='purchase_order_list'),
    path('create/', purchase_order_create, name='purchase_order_create'),
    path('<int:pk>/', purchase_order_detail, name='purchase_order_detail'),
]