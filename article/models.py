
from django.db import models
from django.forms import DateTimeField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Articles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 255, name= "title")
    date = models.DateTimeField(auto_now_add = True)
    thumbnail = models.ImageField( upload_to="articles/thumbnail/")
    def __str__(self):
        return self.title
    content = RichTextUploadingField()
    category = models.CharField(max_length = 255, name = "category")

    class Meta:
        ordering = ['-id']