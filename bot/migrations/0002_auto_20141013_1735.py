# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remember',
            name='type',
            field=models.CharField(max_length=20, choices=[(1, b'Arti'), (2, b'URL')]),
        ),
    ]
