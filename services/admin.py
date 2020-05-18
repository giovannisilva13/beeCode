from django.contrib import admin

from services.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'code', 'name', 'created_at',
    ]
    
admin.site.register(Service, ServiceAdmin)