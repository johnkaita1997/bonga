# Generated by Django 3.2.18 on 2023-05-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20230508_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolwebcreate',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
    ]
