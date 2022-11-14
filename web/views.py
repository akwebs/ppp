from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, BlogCategory, Projects, Contact
from django.contrib import messages
# Create your views here.
def index(request):
    blogs = Blog.objects.all()[0:3]
    projects = Projects.objects.all()[0:3]
    return render(request, 'index.html', {'blogs':blogs, 'projects':projects})

def blog_category(request, slug):
    category = BlogCategory.objects.all()
    blogs = Blog.objects.filter(category__slug=slug)
    return render(request, 'blog.html', {'blogs':blogs, 'category':category})

def blog(request):
    category = BlogCategory.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs':blogs, 'category':category})

def blogdetails(request, slug):
    category = BlogCategory.objects.all()
    blogs = Blog.objects.exclude(slug=slug).all()[0:3]
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_details.html', {'blog':blog, 'blogs':blogs, 'category':category})

def about(request):
    return render(request, 'about.html')

def whatwedo(request):
    return render(request, 'what-do.html')

def projects(request):
    projects = Projects.objects.all()
    return render(request, 'projects.html', {'projects':projects})

def projectdetails(request, slug):
    projects = Projects.objects.exclude(slug=slug).all()[0:3]
    project = get_object_or_404(Projects, slug=slug)
    return render(request, 'project_details.html', {'project':project, 'projects':projects})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        city = request.POST['city']
        country = request.POST['country']
        message = request.POST['message']
        contact = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            city=city,
            country=country,
            message=message
        )
        contact.save()
        messages.success(request, 'Your message has been sent!')
        print('Message sent!', name, email)
        return redirect('web:contact')
    return render(request, 'contact.html')

