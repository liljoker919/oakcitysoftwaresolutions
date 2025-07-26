from django.db import models


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