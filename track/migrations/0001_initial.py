# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllocationRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('percent', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HoldingType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('asset_class', models.CharField(max_length=2, choices=[(b'EQ', b'equity'), (b'BD', b'bond')])),
                ('country', models.CharField(max_length=2, choices=[(b'CA', b'CA'), (b'US', b'US'), (b'IN', b'IN')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='allocationrule',
            name='holding',
            field=models.ForeignKey(to='track.HoldingType'),
            preserve_default=True,
        ),
    ]
