# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '__first__'),
        ('users', '__first__'),
        ('timeline', '0002_auto_20150701_0254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField()),
                ('patient', models.ForeignKey(to='users.Patient')),
                ('prescription', models.OneToOneField(to='dashboard.Prescription')),
            ],
        ),
    ]
