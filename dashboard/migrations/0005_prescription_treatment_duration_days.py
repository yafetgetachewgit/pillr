# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20150807_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='treatment_duration_days',
            field=models.IntegerField(default=3),
        ),
    ]
