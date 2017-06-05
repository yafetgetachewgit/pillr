# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20150810_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prescription',
            old_name='every_x',
            new_name='every',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='amount_per_interval',
        ),
        migrations.AddField(
            model_name='prescription',
            name='total_doses',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prescription',
            name='doses',
            field=models.IntegerField(default=1),
        ),
    ]
