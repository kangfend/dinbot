# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20141013_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remember',
            name='channel',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
