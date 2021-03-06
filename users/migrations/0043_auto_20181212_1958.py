# Generated by Django 2.0.5 on 2018-12-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_auto_20181206_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='taggedskill',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='taggedskill',
            name='tag',
        ),
        migrations.AddField(
            model_name='customuser',
            name='gives_tutorials',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tutorial_area',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='TaggedSkill',
        ),
    ]
