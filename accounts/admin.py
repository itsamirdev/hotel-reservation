from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'is_active', 'is_staff')
    search_fields = ('phone',)
    list_filter = ('is_active',)

