# Generated by Django 4.2.3 on 2023-07-14 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HackathonApp', '0003_alter_hackathontable_hackathon_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathontable',
            name='registered_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hackathontable',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ownhackathons', to=settings.AUTH_USER_MODEL),
        ),
    ]
