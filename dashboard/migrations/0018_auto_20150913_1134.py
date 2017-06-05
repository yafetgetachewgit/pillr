# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20150913_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='drug_name',
            new_name='drug',
        ),
    ]
