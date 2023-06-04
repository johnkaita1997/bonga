# Generated by Django 3.2.18 on 2023-06-01 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        ('constants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='constant',
            name='school',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='constants', to='school.school'),
        ),
    ]
