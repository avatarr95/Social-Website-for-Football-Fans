# Generated by Django 2.2.5 on 2019-12-25 14:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('valverde', '0012_auto_20191217_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_description',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 14, 46, 3, 567342, tzinfo=utc)),
        ),
    ]
