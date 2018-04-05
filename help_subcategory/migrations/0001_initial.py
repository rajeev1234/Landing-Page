# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('help_Qna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Help_SubCategory_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='HelpSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Help_SubCategory_Name', models.CharField(max_length=100)),
                ('Help_SubCategory_Topic_Id', models.CharField(max_length=100)),
                ('Help_SubCategory_Modified_Date', models.DateField(auto_now_add=True)),
                ('Help_SubCategory_Created_Date', models.DateField(auto_now_add=True)),
                ('HelpSubCategory_qna_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='helpsubcategory', to='help_Qna.HelpQna')),
            ],
        ),
    ]
