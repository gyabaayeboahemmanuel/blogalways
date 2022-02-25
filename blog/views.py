from multiprocessing import context
from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import *
from django.urls import reverse
from django.views import generic

from . import forms


class CkEditorFormView(generic.FormView):
    form_class = forms.CkEditorForm
    template_name = "blog/post_blog.html"
    def get_success_url(self):
        return reverse("ckeditor-form")

ckeditor_form_view = CkEditorFormView.as_view()

def blog_post (request):
    blog = Blog.objects.all()
    context = {
        "blog":blog,
    }
    return render(request, "blog/blogs.html", context)
    
def index (request):
    return render (request, "index.html")


def blog_details(request, id):
    blog = get_object_or_404(Blog, id = id)
   
    content ={
        "blog": blog,
    }
    return render (request, "blog/blog_details.html", content)

