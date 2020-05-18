
from django.contrib import admin
from django.urls import path, include

from products.views import products, product_create, product_update, product_delete, product_delete_done, change_stock

app_name = 'products'
urlpatterns = [
    path('produtos/', products, name="products"),
    path('cadastrar-produto/', product_create, name="product_create"),
    path('alterar-produto/<int:pk>/', product_update, name="product_update"),
    path('excluir-produto/<int:pk>/', product_delete, name="product_delete"),
    path('confirmar-exclusao-de-produto/<int:pk>/', product_delete_done, name="product_delete_done"),
    path('alterar-estoque/', change_stock, name="change_stock"),
]
