# Generated by Django 5.2.1 on 2025-06-07 13:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.PositiveIntegerField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
