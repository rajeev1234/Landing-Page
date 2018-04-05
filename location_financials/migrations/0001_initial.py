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
                ('LocationFinancial_Comment', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocationFinancial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocationFinancial_Authority_Charges', models.CharField(max_length=100)),
                ('LocationFinancial_Availability', models.BooleanField(default=False)),
                ('LocationFinancial_Discount_On_Crewsize', models.BooleanField(default=False)),
                ('LocationFinancial_Discount_On_Shoot_Length', models.BooleanField(default=False)),
                ('LocationFinancial_Location_Id', models.CharField(max_length=280)),
                ('LocationFinancial_Monthly_Rate_Crewsize1', models.CharField(max_length=100)),
                ('LocationFinancial_Monthly_Rate_Crewsize2', models.CharField(max_length=100)),
                ('LocationFinancial_Monthly_Rate_Crewsize3', models.CharField(max_length=100)),
                ('LocationFinancial_Monthly_Rate_Crewsize4', models.CharField(max_length=100)),
                ('LocationFinancial_One_Day_Rent_Crewsize1', models.CharField(max_length=100)),
                ('LocationFinancial_One_Day_Rent_Crewsize2', models.CharField(max_length=100)),
                ('LocationFinancial_One_Day_Rent_Crewsize3', models.CharField(max_length=100)),
                ('LocationFinancial_One_Day_Rent_Crewsize4', models.CharField(max_length=100)),
                ('LocationFinancial_Prices_Available', models.BooleanField(default=False)),
                ('LocationFinancial_Student_Rate', models.CharField(max_length=100)),
                ('LocationFinancial_Weekly_Rate_Crewsize1', models.CharField(max_length=100)),
                ('LocationFinancial_Weekly_Rate_Crewsize2', models.CharField(max_length=100)),
                ('LocationFinancial_Weekly_Rate_Crewsize3', models.CharField(max_length=100)),
                ('LocationFinancial_Weekly_Rate_Crewsize4', models.CharField(max_length=100)),
                ('LocationFinancial_Modified_Date', models.DateField(auto_now=True)),
                ('LocationFinancial_Created_Date', models.DateField(auto_now=True)),
            ],
        ),
    ]
