# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 8, 7, 18, 16, 29, 303524, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='doctor',
            field=models.ManyToManyField(to='users.Doctor'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='doses',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='drug_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='patient',
            field=models.ManyToManyField(to='users.Patient'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='treatment_duration_days',
            field=models.IntegerField(default=3),
        ),
    ]
