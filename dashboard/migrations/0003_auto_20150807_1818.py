# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20150807_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='drug_name',
            field=models.CharField(default='not specified', max_length=100),
            preserve_default=False,
        ),
    ]
