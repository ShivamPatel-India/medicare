# Generated by Django 3.1.5 on 2021-04-11 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210411_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_u',
            old_name='messeage',
            new_name='message',
        ),
    ]
