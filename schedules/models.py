
from django.db import models
from django.utils import timezone

from accounts.models import User
from pets.models import Pets
from services.models import Service

class Schedule(models.Model):

    STATUS_CHOICES = (
        ("A", "Agendado"),
        ("T", "Atendido"),
        ("C", "Cancelado"),
    )

    schedule = models.DateTimeField(verbose_name="Data e Horário", auto_now_add=False, blank=True, null=True, default=timezone.now)
    user = models.ForeignKey(User, verbose_name="Cliente", on_delete=models.CASCADE)
    pet = models.ForeignKey(Pets, verbose_name="Animal", on_delete=models.CASCADE)
    service = models.ForeignKey(Service, verbose_name="Serviço", on_delete=models.CASCADE)
    status = models.CharField("Status", max_length=1, choices=STATUS_CHOICES, default="A")

    created_at = models.DateTimeField("Data de Criação", auto_now_add=True)
    updated_at = models.DateTimeField("Data de Alteração", auto_now=True)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
