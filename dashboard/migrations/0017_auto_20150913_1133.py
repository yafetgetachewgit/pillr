# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_remove_prescription_drug_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('drug_name', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='prescription',
            name='drug_name',
            field=models.ForeignKey(to='dashboard.Drug', null=True),
        ),
    ]
