# Generated by Django 2.2.6 on 2019-10-22 16:05

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.get_image_path),
        ),
    ]
