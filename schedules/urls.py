
from django.contrib import admin
from django.urls import path, include

from schedules.views import schedules, schedule_create, schedule_update, schedule_delete, schedule_delete_done

app_name = 'schedules'
urlpatterns = [
    path('agendamentos/', schedules, name="schedules"),
    path('cadastrar-agendamento/', schedule_create, name="schedule_create"),
    path('alterar-agendamento/<int:pk>/', schedule_update, name="schedule_update"),
    path('excluir-agendamento/<int:pk>/', schedule_delete, name="schedule_delete"),
    path('confirmar-exclusao-de-agendamento/<int:pk>/', schedule_delete_done, name="schedule_delete_done"),
]
