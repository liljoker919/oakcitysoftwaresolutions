from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'organization', 'phone_number', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'organization']
    list_filter = ['organization', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number')
        }),
        ('Professional Information', {
            'fields': ('organization', 'title')
        }),
        ('Additional Information', {
            'fields': ('address', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
