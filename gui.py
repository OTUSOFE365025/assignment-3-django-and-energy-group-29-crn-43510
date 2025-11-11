import os
import django
from tkinter import *

# setup django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import Product

def launch_gui():
    window = Tk()
    window.title("Product Scanner")

    # label
    label = Label(window, text="Enter UPC:")
    label.pack()

    # entry box
    upc_entry = Entry(window)
    upc_entry.pack()

    # label to show results
    result_label = Label(window, text="")
    result_label.pack()

    # search function
    def search():
        upc = upc_entry.get()
        try:
            product = Product.objects.get(UPC=upc)
            result_label.config(text=f"Item: {product.name}, Price: ${product.price}")
        except Product.DoesNotExist:
            result_label.config(text="Error: can't find item")

    # search button
    search_button = Button(window, text="Search", command=search)
    search_button.pack()
    #doesnt close immediately
    window.mainloop()
