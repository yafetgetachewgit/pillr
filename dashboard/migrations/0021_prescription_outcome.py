# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_prescription_doses_remaining'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='outcome',
            field=models.IntegerField(default=0, choices=[(1, b'Successful'), (0, b'Failed')]),
        ),
    ]
