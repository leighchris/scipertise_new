# Generated by Django 2.0.5 on 2018-11-15 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20181115_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newskill',
            old_name='skills',
            new_name='newskills',
        ),
    ]
