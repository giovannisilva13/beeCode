from django.contrib import admin

from pets.models import Pets

class PetsAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'type_pet', 'class_pet', 'breed'
    ]

admin.site.register(Pets, PetsAdmin)