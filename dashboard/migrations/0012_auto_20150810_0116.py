# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20150810_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='every',
            new_name='the_time_is_in',
        ),
    ]
