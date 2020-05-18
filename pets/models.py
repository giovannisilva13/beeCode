from django.db import models

from accounts.models import User

class Pets(models.Model):

    PET_CHOICES = (
        ('Cachorro', 'Cachorro'),
        ('Gato', 'Gato'),
        ('Hamster', 'Hamster'),
        ('Pássaro', 'Pássaro'),
        ('Peixe', 'Peixe' )
    )

    CLASS_CHOICES = (
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    )

    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    name_pet = models.CharField('Nome do Pet', max_length=56, null=True, blank=False)
    type_pet = models.CharField("Tipo de Pet", max_length=20, choices=PET_CHOICES)
    class_pet = models.CharField("Porte de Pet", max_length=1, choices=CLASS_CHOICES)
    breed = models.CharField('Raça', max_length=56, null=True, blank=False)
    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"

    def __str__(self):
        return "{} - {} - {} - {} - {}".format(self.user, self.name_pet, self.type_pet, self.class_pet, self.breed)

