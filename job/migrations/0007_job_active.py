# Generated by Django 3.2 on 2021-04-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]