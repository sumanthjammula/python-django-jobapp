# Generated by Django 4.1.4 on 2022-12-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_jobpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='slug',
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]
