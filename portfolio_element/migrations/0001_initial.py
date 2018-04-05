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
                ('portfolio_element_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PortfolioElement_Category', models.CharField(max_length=200)),
                ('PortfolioElement_Director', models.CharField(max_length=200)),
                ('PortfolioElement_Production_House', models.CharField(max_length=200)),
                ('PortfolioElement_Title', models.CharField(max_length=200)),
                ('PortfolioElement_Audio', models.FileField(max_length=200, upload_to='mp3/')),
                ('PortfolioElement_Creator', models.CharField(max_length=200)),
                ('PortfolioElement_Image', models.ImageField(max_length=200, upload_to='')),
                ('PortfolioElement_Performance_Video', models.FileField(upload_to='')),
                ('portfolio_element_Message', models.CharField(max_length=280)),
                ('PortfolioElement_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]