# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0006_auto_20150828_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='prescription',
            field=models.ForeignKey(to='dashboard.Prescription'),
        ),
    ]
