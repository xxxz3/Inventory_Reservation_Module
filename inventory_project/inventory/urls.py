from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_product, name='search_product'),
    path('reserve_product/<product_id>/', views.reserve_product, name='reserve_product'),
]