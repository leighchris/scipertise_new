# Generated by Django 2.0.5 on 2018-11-18 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_customuser_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
    ]
