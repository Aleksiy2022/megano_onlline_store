# Generated by Django 4.2.2 on 2023-08-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='session_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]