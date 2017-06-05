# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_institute_pharmacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='region',
            field=models.CharField(default=b'n/a', max_length=100),
        ),
    ]
