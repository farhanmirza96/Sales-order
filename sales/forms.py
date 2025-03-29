from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from django.forms.widgets import PasswordInput, TextInput
from .models import *

# Register/create user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForms(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['customer', 'rate', 'qty', 'unit', 'delivery', 'product', 'status']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.total_amount = instance.rate * instance.qty  # Calculate total amount
        if commit:
            instance.save()
        return instance
        # or fields = ['customer', 'total_amount', 'status']

class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']

class UpdateSalesOrder(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = ['customer', 'rate', 'qty', 'unit', 'delivery', 'product', 'status']