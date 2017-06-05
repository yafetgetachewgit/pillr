# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20150913_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
    ]
