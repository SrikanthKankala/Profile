# Generated by Django 4.2.6 on 2023-10-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_placelived_place_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='relationship_name_visibility',
            field=models.CharField(blank=True, default='public friends', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='relationship',
            name='relationship_type_visibility',
            field=models.CharField(blank=True, default='public friends', max_length=20, null=True),
        ),
    ]
