# Generated by Django 4.2.3 on 2023-07-15 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HackathonApp', '0004_hackathontable_registered_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissiontable',
            name='submission_link',
            field=models.URLField(blank=True, max_length=128, null=True),
        ),
    ]