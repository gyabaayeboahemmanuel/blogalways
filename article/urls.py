from unicodedata import name
from django.urls import path, re_path
from .views import *
app_name = "article"
urlpatterns = [
    path("", article, name="article" ),
    path("post", post_article, name="post_article"),
    path("<int:id>/article_detail", article_details, name="article_details"),   
]
