# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model', '0001_initial'),
        ('TalentProfile', '0003_talentprofile_talentprofile_mimicry_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='talentprofile',
            name='TalentProfile_Model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.Models'),
        ),
    ]
