from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    path('contacts/', views.ContactListView.as_view(), name='contact_list'),
    path('contacts/<int:pk>/', views.ContactDetailView.as_view(), name='contact_detail'),
]