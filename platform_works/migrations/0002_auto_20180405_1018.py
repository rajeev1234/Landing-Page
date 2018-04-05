# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('platform_works', '0001_initial'),
        ('userdetails', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformworks',
            name='PlatformWorks_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platform_works', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='platformworks',
            name='PlatformWorks_Location_Manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PlatformWorks', to='userdetails.UserDetails'),
        ),
        migrations.AddField(
            model_name='comment',
            name='platform_works_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_works.PlatformWorks'),
        ),
    ]