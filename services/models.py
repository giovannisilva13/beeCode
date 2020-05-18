
from django.db import models

class Service(models.Model):

    code = models.CharField("Código do Serviço", max_length=999, null=False, blank=False)
    name = models.CharField("Nome do Serviço", max_length=256, null=False, blank=False)

    created_at = models.DateTimeField("Data de Criação", auto_now_add=True)
    updated_at = models.DateTimeField("Data de Alteração", auto_now=True)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
    
    def __str__(self):
        return "{} - {}".format(self.code, self.name)
