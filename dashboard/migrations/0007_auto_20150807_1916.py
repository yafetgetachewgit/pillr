# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('dashboard', '0006_remove_prescription_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='doctor',
        ),
        migrations.AddField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(default=1, to='users.Doctor'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='patient',
        ),
        migrations.AddField(
            model_name='prescription',
            name='patient',
            field=models.ForeignKey(default=1, to='users.Patient'),
            preserve_default=False,
        ),
    ]
