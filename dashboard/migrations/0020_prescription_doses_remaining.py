# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_prescription_total_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='doses_remaining',
            field=models.IntegerField(default=0),
        ),
    ]
