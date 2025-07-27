from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('blog/', views.blog_page, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
