# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('help_center', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('help_category', '0002_auto_20180405_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpcenter',
            name='Help_Center_Creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='helpcenter',
            name='Helpcenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='helpcenters', to='help_category.Help_Category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Help_Center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help_center.HelpCenter'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Help_Center_Comment_Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='helpcenter_Comment_Author', to=settings.AUTH_USER_MODEL),
        ),
    ]