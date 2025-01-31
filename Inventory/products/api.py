from ninja import NinjaAPI, Schema
from typing import List
from django.shortcuts import get_object_or_404
from .models import Product, Supplier

api = NinjaAPI()

class SupplierSchema(Schema):
    id: int
    name: str
    contact_info: str

class ProductSchemaIn(Schema):
    name: str
    price: float
    quantity: int
    supplier_id: int

class ProductSchemaOut(Schema):
    id: int
    name: str
    price: float
    quantity: int
    supplier: SupplierSchema

@api.post("/products/", response={201: ProductSchemaOut, 404: dict})
def create_product(request, payload: ProductSchemaIn):
    try:
        supplier = Supplier.objects.get(id=payload.supplier_id)
    except Supplier.DoesNotExist:
        return 404, {"message": "Supplier not found"}

    product = Product.objects.create(supplier=supplier, **payload.dict())
    return 201, product

@api.get("/products/{product_id}", response={200: ProductSchemaOut, 404: dict})
def get_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    return product

@api.get("/products/", response=List[ProductSchemaOut])
def list_products(request):
    return Product.objects.all()

@api.put("/products/{product_id}", response={200: ProductSchemaOut, 404: dict})
def update_product(request, product_id: int, payload: ProductSchemaIn):
    product = get_object_or_404(Product, id=product_id)
    try:
        supplier = Supplier.objects.get(id=payload.supplier_id)
    except Supplier.DoesNotExist:
        return 404, {"message": "Supplier not found"}

    for attr, value in payload.dict().items():
        if attr == 'supplier_id':
            product.supplier = supplier
        else:
            setattr(product, attr, value)
    product.save()
    return product

@api.delete("/products/{product_id}", response={200: dict, 404: dict})
def delete_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return {"success": True}