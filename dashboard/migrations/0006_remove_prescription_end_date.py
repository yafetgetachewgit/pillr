# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_prescription_treatment_duration_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='end_date',
        ),
    ]
