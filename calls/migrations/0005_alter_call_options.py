# Generated by Django 3.2.18 on 2023-05-08 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0004_call_personcalled'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='call',
            options={'ordering': ['-date_created']},
        ),
    ]
