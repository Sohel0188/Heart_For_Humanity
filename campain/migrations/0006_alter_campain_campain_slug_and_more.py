# Generated by Django 5.0.6 on 2025-01-30 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campain', '0005_donate_campaign_alter_donate_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campain',
            name='campain_slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='campain',
            name='raised_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='donate',
            name='campaign',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='donate_set', to='campain.campain'),
        ),
    ]
