from django.db import models

from django.utils import timezone

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções"),
    )

    USER_TYPE = (
        ("C", "Cliente"),
        ("F", "Funcionário"),
    )

    phone = models.IntegerField("Telefone", default=0)
    birth_date = models.DateTimeField("Data de Nascimento", auto_now_add=False, blank=True, null=True, default=timezone.now)
    job_rule = models.CharField("Cargo", max_length=8, null=False, blank=True)
    sex = models.CharField("Sexo", max_length=1, choices=SEXO_CHOICES)
    user_type = models.CharField("Tipo de Usuário", max_length=1, choices=USER_TYPE, default="C")
    cpf = models.CharField("CPF", max_length=11, null=False, blank=False)

    zipcode = models.IntegerField('CEP', default=0, null=True, blank=True)
    street = models.CharField('Rua', max_length=100, null=True, blank=True)
    number = models.IntegerField('Número', default=0, null=True, blank=True)
    complement = models.CharField('Complemento', max_length=100, null=False, blank=True)
    district = models.CharField('Bairro', max_length=30, null=True, blank=True)
    city = models.CharField('Cidade', max_length=30, null=True, blank=True)
    state = models.CharField('Estado', max_length=2, null=True, blank=True)

    created_at = models.DateTimeField("Data de Criação", auto_now_add=True)
    updated_at = models.DateTimeField("Data de Alteração", auto_now=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return "{} - {} - {}".format(self.first_name, self.email, self.get_user_type_display())
    