# Generated by Django 3.1.7 on 2021-03-17 07:02

import django.core.management.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('key', models.CharField(default=django.core.management.utils.get_random_secret_key, max_length=50)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]