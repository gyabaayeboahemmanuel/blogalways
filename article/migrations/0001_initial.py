# Generated by Django 4.0 on 2022-03-04 14:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='articles/thumbnail/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]