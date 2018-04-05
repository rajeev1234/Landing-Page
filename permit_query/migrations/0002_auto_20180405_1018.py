# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('permit_query', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='permitquery',
            name='PermitQuery_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permit_query', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='permit_query_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permit_query.PermitQuery'),
        ),
    ]
