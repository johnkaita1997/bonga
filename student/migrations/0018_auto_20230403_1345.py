# Generated by Django 3.2.18 on 2023-04-03 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='confirmpassword',
            field=models.CharField(blank=True, default='one', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, default='one', max_length=255, null=True),
        ),
    ]
