# Generated by Django 5.1.1 on 2025-04-13 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_vendor',
        ),
    ]
