# Generated by Django 3.2.18 on 2023-04-03 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0016_auto_20230403_0936'),
        ('school', '0002_auto_20230402_1526'),
        ('student', '0010_rename_students_poted'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='poted',
            new_name='Student',
        ),
    ]
