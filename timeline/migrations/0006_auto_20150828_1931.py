# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0005_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(default=2, choices=[(2, b'I am feeling better'), (1, b'No change in my health'), (0, b'I am getting worse')]),
        ),
    ]
