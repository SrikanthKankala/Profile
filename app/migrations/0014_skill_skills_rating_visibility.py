# Generated by Django 4.2.6 on 2023-10-27 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_skill_skills_name_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skills_rating_visibility',
            field=models.CharField(blank=True, default='public friends', max_length=20, null=True),
        ),
    ]
