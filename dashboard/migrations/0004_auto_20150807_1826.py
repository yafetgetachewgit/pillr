# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20150807_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='treatment_duration_days',
        ),
        migrations.AddField(
            model_name='prescription',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 18, 26, 17, 146034, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
