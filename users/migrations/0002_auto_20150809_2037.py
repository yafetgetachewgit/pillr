# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInfo',
        ),
        migrations.AddField(
            model_name='doctor',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='licenced',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(default='unspecified', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='doctors',
            field=models.ManyToManyField(to='users.Doctor'),
        ),
        migrations.AddField(
            model_name='patient',
            name='height',
            field=models.DecimalField(default=1.65, max_digits=3, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.DecimalField(default=65, max_digits=4, decimal_places=2),
            preserve_default=False,
        ),
    ]
