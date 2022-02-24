from django import forms

from .models import *

User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
        )

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("profile_picture",)
