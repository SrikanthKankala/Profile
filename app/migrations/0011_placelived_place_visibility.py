# Generated by Django 4.2.6 on 2023-10-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_contact_overview_contact_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='placelived',
            name='place_visibility',
            field=models.CharField(blank=True, default='public friends', max_length=20, null=True),
        ),
    ]