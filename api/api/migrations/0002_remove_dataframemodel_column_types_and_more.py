# Generated by Django 5.0.3 on 2024-03-06 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataframemodel',
            name='column_types',
        ),
        migrations.RemoveField(
            model_name='dataframemodel',
            name='file_path',
        ),
    ]
