# Generated by Django 4.2.6 on 2023-10-25 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=255)),
                ('about_des', models.CharField(max_length=255)),
                ('title_visibility', models.CharField(default='everyone', max_length=20)),
                ('description_visibility', models.CharField(default='everyone', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ach_title', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('ach_des', models.TextField()),
                ('image', models.ImageField(upload_to='achievements/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_number', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('lives_in', models.CharField(max_length=100, null=True)),
                ('last_studied_in', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('total_experience', models.IntegerField(null=True)),
                ('relationship_status', models.CharField(max_length=20, null=True)),
                ('languages', models.CharField(max_length=100, null=True)),
                ('birthday', models.DateField(null=True)),
                ('website', models.URLField(null=True)),
                ('religion', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_college', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('field_of_study', models.CharField(max_length=100)),
                ('university_name', models.CharField(max_length=100)),
                ('edu_start_date', models.DateField()),
                ('edu_end_date', models.DateField()),
                ('edu_des', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, null=True)),
                ('company_name', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('ex_start_date', models.DateField(null=True)),
                ('ex_end_date', models.DateField(null=True)),
                ('ex_des', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceLived',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=100, null=True)),
                ('place_start_date', models.DateField(blank=True, null=True)),
                ('place_end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('relationship_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(blank=True, max_length=50, null=True)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_title', models.CharField(blank=True, max_length=100, null=True)),
                ('work_des', models.TextField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]