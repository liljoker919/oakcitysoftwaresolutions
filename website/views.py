from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactSubmissionForm
from .models import BlogPost
from django.contrib import messages


# Home Page
def home_page(request):
    # contact view
    if request.method == 'POST':
        form = ContactSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your contact submission has been received.")
            return redirect('home') 
        else:
            messages.error(request,"There was a problem with your submission. Please correct the errors below.")
    else:
        form = ContactSubmissionForm()

    return render(request,'website/index.html',{'form': form})


# Blog List Page
def blog_page(request):
    # Get all published blog posts ordered by published date
    published_posts = BlogPost.objects.filter(status='published', published_date__isnull=False).order_by('-published_date')
    return render(request, 'website/blog.html', {'posts': published_posts})


# Blog Detail Page
def blog_detail(request, slug):
    # Get the specific published blog post
    post = get_object_or_404(BlogPost, slug=slug, status='published', published_date__isnull=False)
    return render(request, 'website/blog_detail.html', {'post': post})
