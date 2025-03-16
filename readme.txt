virtualenv venv
pip install Django django-crispy-forms Pillow
django-admin startproject sales_purchase_app .
django-admin startapp accounts
django-admin startapp sales
django-admin startapp purchases
django-admin startapp inventory
INSTALLED_APPS = [
    ...
    'accounts',
    'sales',
    'purchases',
    'inventory',
    'crispy_forms',
]
creat models than
python manage.py makemigrations
python manage.py migrate
register in file admin.py noth sale and purchase apps folder
    from .models import SalesOrder

    # Register your models here.
    admin.site.register(SalesOrder)
python manage.py createsuperuser
python manage.py runserver
