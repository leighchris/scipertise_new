# Generated by Django 2.0.5 on 2018-11-16 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_remove_customuser_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='skills',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
