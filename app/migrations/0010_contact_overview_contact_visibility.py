# Generated by Django 4.2.6 on 2023-10-26 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_experience_ex_jobtitle_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='overview_contact_visibility',
            field=models.CharField(blank=True, default='public friends', max_length=20, null=True),
        ),
    ]