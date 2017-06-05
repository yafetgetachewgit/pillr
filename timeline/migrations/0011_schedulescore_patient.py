# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_institute_pharmacy'),
        ('timeline', '0010_auto_20150914_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulescore',
            name='patient',
            field=models.ForeignKey(default=1, to='users.Patient'),
            preserve_default=False,
        ),
    ]
