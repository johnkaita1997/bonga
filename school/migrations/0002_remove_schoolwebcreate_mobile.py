# Generated by Django 3.2.18 on 2023-06-01 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolwebcreate',
            name='mobile',
        ),
    ]
