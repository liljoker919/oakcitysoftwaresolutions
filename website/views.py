from django.shortcuts import render,redirect
from .forms import ContactSubmissionForm
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


# Blog Page
def blog_page(request):
    return render(request,'website/blog.html')
