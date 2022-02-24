import imp
from unicodedata import name
from django.urls import path, re_path
from .views import *
app_name = "user"
urlpatterns = [
    path("signup", signup, name="signup"), 
    path("<int:id>/profile", view_profile, name="view_profile"),   
]