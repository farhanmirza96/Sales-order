from django.shortcuts import render

# Create your views here.
def accounts(request):
    return render(request, 'accounts/accounts.html')  # Create this template