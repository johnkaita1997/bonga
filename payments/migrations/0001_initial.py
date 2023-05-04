# Generated by Django 3.2.18 on 2023-04-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaCheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(blank=True, null=True)),
                ('user', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('mobile', models.CharField(max_length=255)),
            ],
        ),
    ]
