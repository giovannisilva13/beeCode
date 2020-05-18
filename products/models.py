
from django.db import models
from django.contrib.auth.models import AbstractUser

class Product(models.Model):

    code = models.CharField("Código do Produto", max_length=999, null=False, blank=False)
    name = models.CharField("Nome do Produto", max_length=256, null=False, blank=False)
    price = models.FloatField("Preço", default=0)
    quantity = models.IntegerField("Quantidade em Estoque", default=0)
    stock_entry = models.IntegerField("Entrada em Estoque", default=0)
    stock_exit = models.IntegerField("Saída em Estoque", default=0)

    created_at = models.DateTimeField("Data de Criação", auto_now_add=True)
    updated_at = models.DateTimeField("Data de Alteração", auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
    def __str__(self):
        return "{} - {} - {}".format(self.name, self.quantity, self.price)

    def get_current_quantity(self):
        self.quantity = self.stock_entry - self.stock_exit
        self.save()
        return self.quantity