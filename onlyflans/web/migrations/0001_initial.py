# Generated by Django 5.1.2 on 2024-10-24 04:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flan_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(default='No description')),
                ('image_url', models.URLField()),
                ('slug', models.SlugField(unique=True)),
                ('is_private', models.BooleanField()),
            ],
        ),
    ]