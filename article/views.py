from email import message
from importlib.metadata import files
from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from django.urls import reverse
from django.views import generic

from .forms import *


# class CkEditorFormView(generic.FormView):
#     form_class = forms.CkEditorForm
#     template_name = "article/post_article.html"
#     def get_success_url(self):
#         return reverse("ckeditor-form")

# ckeditor_form_view = CkEditorFormView.as_view()


def article (request):
    articles = Articles.objects.all()
    #search
    search_item = request.GET.get('search_item')
    if search_item != '' and search_item != None:
        articles = articles.filter(title__icontains = search_item)
    context = {
        "articles":articles,
    }
    return render(request, "article/articles.html", context)
    
def index (request):
    return render (request, "index.html")


def article_details(request, id):
    article = get_object_or_404(Articles, id = id)
   
    content ={
        "articles": article,
    }
    return render (request, "article/article_details.html", content)

@login_required
def post_article(request):
    if request.method == "POST":
        postarticleforms = post_article_forms(data= request.POST, files=request.FILES)
        if postarticleforms.is_valid():
            postarticle =  postarticleforms.save(commit=False)
            postarticle.author = request.user
            postarticle.save()
            message.success(request, 'Post Created')
            return redirect("/articles/")
        else:
            message.warning(request, "Invalid data entry")
    else: 
        postarticleforms = post_article_forms()
    context ={
        "postarticleforms": postarticleforms,
    }
    return render(request, "article/post_article.html", context)