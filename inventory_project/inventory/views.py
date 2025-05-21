from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db import transaction
from django.core.cache import cache
from .models import Product
from .services import reserve_product_service

def search_product(request):
    query = request.GET.get('query', '')
    cache_key = f'search_product_{query}'
    cached_data = cache.get(cache_key)

    if cached_data:
        return JsonResponse(cached_data, safe=False)
    else:
        products = Product.objects.filter(name__icontains=query) | Product.objects.filter(product_id__icontains=query)
        data = [{'product_id': product.product_id, 'name': product.name, 'inventory': product.inventory} for product in products]
        cache.set(cache_key, data, 300)  # Cache for 5 minutes
        return JsonResponse(data, safe=False)

@transaction.atomic
def reserve_product(request, product_id):
    try:
        result = reserve_product_service(product_id)
        return JsonResponse(result, status=200 if result['status'] == 'success' else 400)
    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)