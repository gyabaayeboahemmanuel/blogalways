from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Profile (models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to = "profile/")
    dateSignedUp = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ("-user",)
    def __str__(self) -> str:
        return self.user.first_name + " "+ self.user.last_name