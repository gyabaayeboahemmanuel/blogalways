# Generated by Django 4.0 on 2022-04-05 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile2_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile2',
            name='lastName',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
