
from django.contrib import admin
from django.urls import path, include

from accounts.views import (
    clients, client_create, client_update, client_delete, client_delete_done,
    employees, employee_create, employee_update, employee_delete, employee_delete_done,
    change_password
)

app_name = 'accounts'
urlpatterns = [
    path('clientes', clients, name="clients"),
    path('cadastrar-cliente/', client_create, name="client_create"),
    path('alterar-cliente/<int:pk>/', client_update, name="client_update"),
    path('excluir-cliente/<int:pk>/', client_delete, name="client_delete"),
    path('confirmar-exclusao-de-cliente/<int:pk>/', client_delete_done, name="client_delete_done"),

    path('funcionarios', employees, name="employees"),
    path('cadastrar-funcionario/', employee_create, name="employee_create"),
    path('alterar-funcionario/<int:pk>/', employee_update, name="employee_update"),
    path('excluir-funcionario/<int:pk>/', employee_delete, name="employee_delete"),
    path('confirmar-exclusao-de-funcionario/<int:pk>/', employee_delete_done, name="employee_delete_done"),

    path('alterar-senha/', change_password, name="change_password"),
]
