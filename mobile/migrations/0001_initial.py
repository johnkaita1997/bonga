# Generated by Django 3.2.18 on 2023-06-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('standingtoken', models.FloatField(blank=True, default=0.0, max_length=255, null=True)),
                ('standingminutes', models.FloatField(blank=True, default=0.0, max_length=255, null=True)),
                ('tokensconsumed', models.FloatField(blank=True, default=0.0, max_length=255, null=True)),
                ('minutesconsumed', models.FloatField(blank=True, default=0.0, max_length=255, null=True)),
                ('active', models.BooleanField(default=True, max_length=255)),
                ('mobile', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
