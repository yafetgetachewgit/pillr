# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('timeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='patient',
            field=models.ForeignKey(default=None, to='users.Patient'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='prescription',
            field=models.OneToOneField(to='dashboard.Prescription'),
        ),
    ]
