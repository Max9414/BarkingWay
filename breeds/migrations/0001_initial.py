# Generated by Django 5.0.6 on 2024-06-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('excerpt', models.CharField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
