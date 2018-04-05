# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FilmLocationFromGuidedWithSerial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmlocationfromguidedwithserial',
            name='FilmLocationFromGuidedWithSerial_Creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filmlocationfromguideds', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='filmlocationfromguidedwithserial',
            name='FilmLocationFromGuidedWithSerial_Tourguide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FilmLocationFromGuidedWithSerial', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_FilmLocationFromGuidedWithSerial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsFilmLocationFromGuidedWithSerial', to='FilmLocationFromGuidedWithSerial.FilmLocationFromGuidedWithSerial'),
        ),
        migrations.AddField(
            model_name='comment',
            name='FilmLocationFromGuidedWithSerial_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssFilmLocationFromGuidedWithSerial', to=settings.AUTH_USER_MODEL),
        ),
    ]
