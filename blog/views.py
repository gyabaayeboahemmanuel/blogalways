from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from .models import *

def blog_post (request):
    blog = Blog.objects.all()
    context = {
        "blog":blog,
    }
    return render(request, "blog/blogs.html", context)
    
def index (request):
    return render (request, "index.html")
def blog_details(request, pk):
    blog = Blog.objects.all()
    #for blog_d in blog
    content ={
        
    }
    return render (request, "blog/blog_details.html" ,content)