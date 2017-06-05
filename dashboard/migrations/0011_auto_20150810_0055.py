# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20150810_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='time_between_treatments',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='every',
            field=models.CharField(default=b'DD', max_length=2, choices=[(b'HR', b'Hour(s)'), (b'DD', b'Day(s)'), (b'WK', b'Week(s)'), (b'MM', b'Month(s)'), (b'YY', b'Year(s)')]),
        ),
    ]
