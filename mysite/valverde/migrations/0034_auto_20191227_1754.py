# Generated by Django 2.2.5 on 2019-12-27 16:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('valverde', '0033_auto_20191227_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcomment',
            name='description',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='pic_nr',
            field=models.IntegerField(blank=True, default=9),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 27, 16, 54, 46, 297530, tzinfo=utc)),
        ),
    ]