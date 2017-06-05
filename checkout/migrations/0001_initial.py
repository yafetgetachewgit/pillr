# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrescriptionStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('checkedOut', models.BooleanField(default=False)),
                ('prescription', models.ForeignKey(to='dashboard.Prescription')),
            ],
        ),
    ]
