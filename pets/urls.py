
from django.contrib import admin
from django.urls import path, include

from pets.views import pets, pet_create, pet_update, pet_delete, pet_delete_done

app_name = 'pets'
urlpatterns = [
    path('animais/', pets, name="pets"),
    path('cadastrar-animal/', pet_create, name="pet_create"),
    path('alterar-animal/<int:pk>/', pet_update, name="pet_update"),
    path('excluir-animal/<int:pk>/', pet_delete, name="pet_delete"),
    path('confirmar-exclusao-de-animal/<int:pk>/', pet_delete_done, name="pet_delete_done"),
]
