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
                ('location_psndc_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='LocationPSnDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocationPSnDC_Dc_Office', models.CharField(max_length=100)),
                ('LocationPSnDC_Dcp_Office', models.CharField(max_length=100)),
                ('LocationPSnDC_Location_Id', models.CharField(max_length=100)),
                ('LocationPSnDC_Police_Station', models.CharField(max_length=100)),
                ('LocationPSnDC_Modified_Date', models.DateField(auto_now_add=True)),
                ('LocationPSnDC_Created_Date', models.DateField(auto_now_add=True)),
                ('LocationPSnDC_Message', models.CharField(max_length=280)),
            ],
        ),
    ]