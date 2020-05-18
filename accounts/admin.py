from django.contrib import admin

from accounts.models import User
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email', 'first_name', 'user_type', 'is_superuser'
    ]

admin.site.register(User, UserAdmin)