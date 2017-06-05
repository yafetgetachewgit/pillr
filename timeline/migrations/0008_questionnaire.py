# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0007_auto_20150828_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=100)),
                ('choices', models.CharField(max_length=100)),
                ('answers', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]
