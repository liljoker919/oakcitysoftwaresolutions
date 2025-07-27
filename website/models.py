from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    class Meta:
        ordering = ['-published_date', '-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})


class ContactSubmission(models.Model):
    SERVICE_CHOICES = [
        ('Custom Website Development', 'Custom Website Development'),
        ('Website Maintenance', 'Website Maintenance'),
        ('Hosting Services', 'Hosting Services'),
        ('design', 'UI/UX Design'),
        ('SEO Optimization', 'SEO Optimization'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=250)
    email = models.EmailField()
    business_name = models.CharField(max_length=250, blank=True, null=True)
    service_required = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    submission_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email}) - {self.get_service_required_display()}"