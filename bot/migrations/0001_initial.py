# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('channel', models.CharField(max_length=50)),
                ('created', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Remember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=30)),
                ('word', models.CharField(max_length=50)),
                ('penghubung', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('channel', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20, choices=[(b'arti', b'Arti'), (b'url', b'URL')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
