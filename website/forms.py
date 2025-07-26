from django import forms
from .models import ContactSubmission

class ContactSubmissionForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'business_name', 'service_required']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Business Name (optional)'}),
            'service_required': forms.Select(attrs={'class': 'form-control'}),
        }
        