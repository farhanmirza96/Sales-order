from django.urls import path
from . import views
from .views import product_list, product_create, product_detail, inventory 

urlpatterns = [
    path('home/', views.inventory, name='inventory'),
    path('', product_list, name='product_list'),
    path('create/', product_create, name='product_create'),
    path('<int:pk>/', product_detail, name='product_detail'),
]