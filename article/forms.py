from mimetypes import knownfiles
from pyexpat import model
from django import forms
from django.db.models import fields
from .models import *
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingFormField


class CkEditorForm(forms.Form):
    ckeditor_standard_example = RichTextFormField()
    ckeditor_upload_example = RichTextUploadingFormField(
        config_name="my-custom-toolbar"
    )

    
class post_article_forms (forms.ModelForm):
    class Meta: 
        model = Articles
        fields = ("title",
        "image1", "content_part1",
        "image2", "content_part2",
        "image3", "content_part3",
        "image4", "content_part4",
        "image5", "content_part5",
        "image6", "content_part6",
        "category")

