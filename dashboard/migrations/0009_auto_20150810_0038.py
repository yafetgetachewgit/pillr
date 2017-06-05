# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_frequencychoices'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FrequencyChoices',
        ),
        migrations.AddField(
            model_name='prescription',
            name='amount_per_interval',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='prescription',
            name='every_x',
            field=models.CharField(default=b'DD', max_length=2, choices=[(b'HR', b'Hour'), (b'DD', b'Day'), (b'WK', b'Week'), (b'MM', b'Month'), (b'YY', b'Year')]),
        ),
    ]
