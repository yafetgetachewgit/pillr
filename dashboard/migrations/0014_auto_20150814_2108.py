# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20150810_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
