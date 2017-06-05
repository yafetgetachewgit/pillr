# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField()),
                ('comment', models.CharField(max_length=300)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('prescription', models.ForeignKey(to='dashboard.Prescription')),
            ],
        ),
    ]
