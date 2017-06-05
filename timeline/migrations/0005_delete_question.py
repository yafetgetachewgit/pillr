# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_question'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
