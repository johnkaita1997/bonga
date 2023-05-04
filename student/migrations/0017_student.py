# Generated by Django 3.2.18 on 2023-04-03 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20230402_1526'),
        ('student', '0016_delete_soko'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('fullname', models.CharField(max_length=255)),
                ('kcpeindexnumber', models.CharField(blank=True, max_length=255, null=True)),
                ('registrationnumber', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=False, max_length=255)),
                ('activefromdate', models.DateTimeField(blank=True, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(max_length=255)),
                ('confirmpassword', models.CharField(max_length=255)),
                ('tokenbalance', models.FloatField(blank=True, default=0.0, null=True)),
                ('totalnumberofcalls', models.FloatField(blank=True, default=0.0, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('contacts', models.ManyToManyField(related_name='students', to='student.Contact')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.school')),
            ],
        ),
    ]
