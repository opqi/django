# Generated by Django 2.2.6 on 2019-10-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.Category'),
        ),
    ]
