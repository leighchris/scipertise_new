# Generated by Django 2.0.5 on 2018-11-17 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_customuser_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='name',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='skills',
        ),
    ]
