# Generated by Django 3.2.18 on 2023-06-01 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='SchoolWebCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('mobile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='schoolwebcreate', to='mobile.mobile')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
