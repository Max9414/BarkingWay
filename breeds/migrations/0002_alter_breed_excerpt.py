# Generated by Django 5.0.6 on 2024-06-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='excerpt',
            field=models.TextField(),
        ),
    ]
