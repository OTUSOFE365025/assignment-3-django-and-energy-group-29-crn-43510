############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

# Seed a few users in the database
Product.objects.all().delete();  # Clear existing users

Product.objects.create(UPC='12345', name='Coffee', price=8.32)
Product.objects.create(UPC='67890', name='Muffin', price=2.53)
Product.objects.create(UPC='12346', name='Tea', price=4.99)
Product.objects.create(UPC='67891', name='Donut', price=1.99)
Product.objects.create(UPC='12347', name='Chai', price=5.99)
Product.objects.create(UPC='67892', name='Croissant', price=0.99)
Product.objects.create(UPC='12348', name='IcedTea', price=4.99)
Product.objects.create(UPC='67893', name='Bagel', price=0.99)



for u in Product.objects.all():
    print(f'UPC: {u.UPC} \tUsername: {u.name} \tPrice: ${u.price}')
