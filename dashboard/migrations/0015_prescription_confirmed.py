# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20150814_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
