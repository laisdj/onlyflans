# Generated by Django 5.1.2 on 2024-10-25 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contactform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='message',
        ),
    ]