# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20150810_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='time_between_treatments',
            field=models.FloatField(default=1),
        ),
    ]
