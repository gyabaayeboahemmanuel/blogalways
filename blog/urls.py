import imp
from unicodedata import name
from django.urls import path
from .views import *
app_name = "blog"
urlpatterns = [
    path("", blog_post, name="blog_post" ),
    path("<int:pk>/blog_detail", blog_details, name="blog_details"),
]
