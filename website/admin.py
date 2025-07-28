from django.contrib import admin
from .models import ContactSubmission, BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_date', 'created_at')
    list_filter = ('status', 'published_date', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        if obj.status == 'published' and not obj.published_date:
            from django.utils import timezone
            obj.published_date = timezone.now()
        super().save_model(request, obj, form, change)


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'business_name', 'service_required', 'submission_timestamp')
    search_fields = ('name', 'email', 'business_name', 'service_required')
    list_filter = ('service_required', 'submission_timestamp')
