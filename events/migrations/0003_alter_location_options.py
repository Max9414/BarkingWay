# Generated by Django 5.0.6 on 2024-06-06 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_location_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['location']},
        ),
    ]