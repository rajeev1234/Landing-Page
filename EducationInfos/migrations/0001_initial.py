# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EducationInfo_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EducationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EducationInfo_Course', models.CharField(max_length=100)),
                ('EducationInfo_Course_Detail', models.CharField(max_length=100)),
                ('EducationInfo_Institute', models.CharField(max_length=100)),
                ('EducationInfo_Passing_Year', models.CharField(max_length=100)),
                ('EducationInfo_Modified_Date', models.DateField(auto_now_add=True)),
                ('EducationInfo_Created_Time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
