# Generated by Django 5.0.6 on 2025-01-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('contact_for', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Form',
            },
        ),
        migrations.CreateModel(
            name='Contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('facebook_link', models.URLField()),
                ('youtube_link', models.URLField()),
                ('linkedIn_link', models.URLField()),
                ('map', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Information',
            },
        ),
    ]
