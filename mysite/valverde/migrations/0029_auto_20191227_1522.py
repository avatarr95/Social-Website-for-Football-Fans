# Generated by Django 2.2.5 on 2019-12-27 14:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('valverde', '0028_auto_20191227_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic_nr',
            field=models.IntegerField(blank=True, default=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 27, 14, 22, 3, 509678, tzinfo=utc)),
        ),
    ]
