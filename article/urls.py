from unicodedata import name
from django.urls import path, re_path
from .views import *
app_name = "article"
urlpatterns = [
    path("", article_post, name="article_post" ),
    path("d", ckeditor_form_view, name="ckeditor-form"),
    path("<int:id>/article_detail", article_details, name="article_details"),   
]
