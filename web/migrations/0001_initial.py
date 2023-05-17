# Generated by Django 3.2.18 on 2023-05-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImportParentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_fullname_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('parent_phone_number_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('mobiletwo_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('email_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('header_row_number', models.IntegerField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ImportStudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_fullname_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('student_firstname_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('student_middlename_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('student_lastname_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('student_admission_number_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('student_kcpeindex_number_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('parent_fullname_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('parent_phone_number_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('contact_person_one_fullname_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('contact_person_one_mobile_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('contact_person_two_fullname_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('contact_person_two_mobile_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('contact_person_three_fullname_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('contact_person_three_mobile_table_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('header_row_number', models.IntegerField(default=None, max_length=255)),
            ],
        ),
    ]
