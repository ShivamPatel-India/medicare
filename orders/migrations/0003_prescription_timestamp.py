# Generated by Django 3.1.5 on 2021-04-11 10:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
