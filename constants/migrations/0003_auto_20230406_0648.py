# Generated by Django 3.2.18 on 2023-04-06 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constants', '0002_alter_constant_tokennumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constant',
            name='minutepershilling',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='constant',
            name='minutespertokenOrequivalentminutes',
            field=models.FloatField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='constant',
            name='shillingspertokenOrequivalentshillings',
            field=models.FloatField(default=0, max_length=255),
        ),
    ]
