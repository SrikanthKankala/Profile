# Generated by Django 4.2.6 on 2023-10-25 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_about_description_visibility_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description_visibility',
            field=models.CharField(blank=True, default='public friends', max_length=20, null=True),
        ),
    ]
