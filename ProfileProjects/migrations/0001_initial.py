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
                ('ProfileProjects_Comment', models.CharField(max_length=150)),
                ('ProfileProjects_Comment_Created_On', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProfileProjects_Category', models.CharField(max_length=200)),
                ('ProfileProjects_Director', models.CharField(max_length=200)),
                ('ProfileProjects_Production_House', models.CharField(max_length=200)),
                ('ProfileProjects_Title', models.CharField(max_length=200)),
                ('ProfileProjects_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
