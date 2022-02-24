import imp
from unicodedata import name
from django.urls import path, re_path
from .views import *
app_name = "blog"
urlpatterns = [
    path("", blog_post, name="blog_post" ),
    path("d", ckeditor_form_view, name="ckeditor-form"),
    path("<int:id>/blog_detail", blog_details, name="blog_details"),   
]
