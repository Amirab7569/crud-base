# Generated by Django 4.2.17 on 2024-12-30 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
    ]
