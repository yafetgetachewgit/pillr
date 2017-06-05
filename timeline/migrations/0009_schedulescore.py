# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_auto_20150913_1134'),
        ('timeline', '0008_questionnaire'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=2, choices=[(0, b'You missed taking this prescription'), (1, b'You were late in taking this prescription'), (2, b'You have taken this drug on time')])),
                ('prescription_missed', models.DateTimeField(null=True)),
                ('prescription', models.ForeignKey(to='dashboard.Prescription')),
            ],
        ),
    ]
