# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20150807_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequencyChoices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('every_x', models.CharField(default=b'DD', max_length=2, choices=[(b'HR', b'Hour'), (b'DD', b'Day'), (b'WK', b'Week'), (b'MM', b'Month'), (b'YY', b'Year')])),
            ],
        ),
    ]
