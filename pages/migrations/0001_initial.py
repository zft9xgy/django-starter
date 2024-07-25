# Generated by Django 5.0.6 on 2024-07-23 11:30

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='SeoMeta',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=255, null=True)),
                ('index', models.BooleanField(default=True)),
                ('follow', models.BooleanField(default=True)),
                ('page', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seo', to='pages.page', verbose_name='SEO metadata')),
            ],
        ),
    ]
