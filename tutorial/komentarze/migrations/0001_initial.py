# Generated by Django 4.2.11 on 2024-05-03 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=100)),
                ('date_creation', models.DateTimeField()),
                ('date_published', models.DateTimeField()),
            ],
        ),
    ]
