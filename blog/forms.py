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

    
class postblogforms (forms.ModelForm):
    class Meta: 
        model = Blog
        fields = ("title",)

