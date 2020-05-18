from django.contrib import admin

from schedules.models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        'schedule', 'user', 'service', 'pet', 'status'
    ]
    
admin.site.register(Schedule, ScheduleAdmin)