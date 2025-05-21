from django.shortcuts import get_object_or_404
from .models import Product

def reserve_product_service(product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if product.inventory > 0:
        product.inventory -= 1
        product.save()
        return {'status': 'success', 'message': 'Product reserved successfully'}
    else:
        return {'status': 'error', 'message': 'Insufficient stock'}