# Generated by Django 5.0 on 2023-12-08 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('date', models.DateField()),
                ('fighter', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='fighters.fighter')),
            ],
        ),
    ]
