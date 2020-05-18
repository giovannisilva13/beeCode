
from django.contrib import admin
from django.urls import path, include

from services.views import services, service_create, service_update, service_delete, service_delete_done

app_name = 'services'
urlpatterns = [
    path('servicos/', services, name="services"),
    path('cadastrar-servico/', service_create, name="service_create"),
    path('alterar-servico/<int:pk>/', service_update, name="service_update"),
    path('excluir-servico/<int:pk>/', service_delete, name="service_delete"),
    path('confirmar-exclusao-de-servico/<int:pk>/', service_delete_done, name="service_delete_done"),
]
