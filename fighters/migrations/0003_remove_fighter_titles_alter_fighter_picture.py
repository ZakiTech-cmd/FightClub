# Generated by Django 5.0 on 2023-12-14 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighters', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fighter',
            name='titles',
        ),
        migrations.AlterField(
            model_name='fighter',
            name='picture',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]
