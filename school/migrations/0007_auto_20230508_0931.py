# Generated by Django 3.2.18 on 2023-05-08 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_schoolwebcreate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterModelOptions(
            name='schoolwebcreate',
            options={'ordering': ['-date_created']},
        ),
    ]
