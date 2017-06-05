# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0009_schedulescore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulescore',
            name='prescription_missed',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 14, 12, 30, 54, 99063, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
