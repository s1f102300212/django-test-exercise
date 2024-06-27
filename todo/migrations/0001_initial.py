# Generated by Django 5.0.6 on 2024-06-27 08:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('posted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
