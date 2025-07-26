from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'business_name', 'service_required', 'submission_timestamp')
    search_fields = ('name', 'email', 'business_name', 'service_required')
    list_filter = ('service_required', 'submission_timestamp')
