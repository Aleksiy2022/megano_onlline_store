# Generated by Django 4.2.2 on 2023-07-11 18:08

import api_catalog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to=api_catalog.models.category_image_directory_path)),
                ('alt', models.CharField(max_length=200)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='api_catalog.category')),
            ],
        ),
    ]