# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_prescription_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='drug_name',
        ),
    ]
