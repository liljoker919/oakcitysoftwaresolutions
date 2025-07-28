from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


class ContactListView(ListView):
    model = Contact
    template_name = 'crm/contact_list.html'
    context_object_name = 'contacts'
    paginate_by = 20


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'crm/contact_detail.html'
    context_object_name = 'contact'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm(instance=self.object)
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ContactForm(request.POST, instance=self.object)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Contact {self.object} updated successfully!')
            return redirect('crm:contact_detail', pk=self.object.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
            context = self.get_context_data()
            context['form'] = form
            return render(request, self.template_name, context)
