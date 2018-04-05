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
                ('musician_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Musician_Daily_Charges', models.CharField(max_length=200)),
                ('Musician_Description', models.CharField(max_length=500)),
                ('Musician_Financial_Available', models.BooleanField(default=False)),
                ('Musician_Genre', models.CharField(max_length=200)),
                ('Musician_Instrument', models.CharField(max_length=100)),
                ('Musician_ID', models.CharField(max_length=200)),
                ('musician_Message', models.CharField(max_length=280)),
                ('Musician_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
