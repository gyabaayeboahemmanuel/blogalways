# Generated by Django 4.0 on 2022-02-24 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_delete_examplemodel_delete_examplenonuploadmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
