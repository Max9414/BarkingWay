# Generated by Django 5.0.6 on 2024-06-08 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_location_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['event_date']},
        ),
    ]
