# Generated by Django 3.2.18 on 2023-05-08 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constants', '0007_alter_constant_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='constant',
            options={'ordering': ['-date_created']},
        ),
    ]
