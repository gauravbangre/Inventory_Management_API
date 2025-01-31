from django.contrib import admin
from .models import Product, Supplier

# Register the Supplier model
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_info')  # Fields to display in the list view
    search_fields = ('name',)  # Enable search by name
    list_per_page = 20  # Number of items per page

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'supplier')  # Fields to display in the list view
    list_filter = ('supplier',)  # Enable filtering by supplier
    search_fields = ('name', 'supplier__name')  # Enable search by product name or supplier name
    list_per_page = 20  # Number of items per page

    # Customize how the supplier field is displayed in the admin form
    raw_id_fields = ('supplier',)  # Use a search widget for the supplier field
    
