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
                ('mimicry_artist_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MimicryArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MimicryArtist_Daily_Financials', models.CharField(max_length=200)),
                ('MimicryArtist_Description', models.CharField(max_length=500)),
                ('MimicryArtist_Financials_Available', models.BooleanField()),
                ('MimicryArtist_Language', models.CharField(max_length=100)),
                ('MimicryArtist_ID', models.CharField(max_length=100)),
                ('MimicryArtist_Voices', models.CharField(max_length=200)),
                ('MimicryArtist_Message', models.CharField(max_length=280)),
                ('MimicryArtist_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]