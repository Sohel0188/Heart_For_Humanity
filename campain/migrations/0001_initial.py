# Generated by Django 5.0.6 on 2025-01-15 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_useraccount_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campain_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=60)),
                ('image', models.ImageField(upload_to='./media/campain/')),
            ],
        ),
        migrations.CreateModel(
            name='Campain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('image', models.ImageField(upload_to='./media/campain/')),
                ('short_details', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('goal_price', models.FloatField()),
                ('raised_price', models.FloatField()),
                ('campain_day', models.IntegerField()),
                ('donar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.useraccount')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campain.campain_category')),
            ],
        ),
    ]
