from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['uid', 'phone', 'email', 'user', 'is_upgrade', 'upgrade_time', 'expire_time', 'upgrade_count']
    search_fields = ['uid', 'phone', 'email', 'user']
    list_filter = ['is_upgrade', 'upgrade_time', 'expire_time', 'upgrade_count', 'created_at', 'updated_at']
    list_display_links = ['uid', 'phone', 'email', 'user']
    date_hierarchy = 'created_at'
    ordering = ['created_at']
    readonly_fields = ['uid', 'created_at', 'updated_at']


admin.site.register(Profile, ProfileAdmin)
