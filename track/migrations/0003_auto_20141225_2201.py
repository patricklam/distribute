# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_auto_20141225_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('account_type', models.CharField(max_length=2, choices=[(b'RRSP', b'rrsp'), (b'TFSA', b'TFSA'), (b'NR', b'NR')])),
                ('can_add_money', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LocationRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField()),
                ('account_type', models.CharField(max_length=2, choices=[(b'RRSP', b'rrsp'), (b'TFSA', b'TFSA'), (b'NR', b'NR')])),
                ('holding_type', models.ForeignKey(to='track.HoldingType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='allocationrule',
            old_name='holding',
            new_name='holding_type',
        ),
        migrations.RenameField(
            model_name='holding',
            old_name='holding',
            new_name='holding_type',
        ),
        migrations.AddField(
            model_name='holding',
            name='account',
            field=models.ForeignKey(default=None, to='track.Account'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='holdingtype',
            name='asset_class',
            field=models.CharField(max_length=2, choices=[(b'EQ', b'equity'), (b'BD', b'bond'), (b'$$', b'cash')]),
            preserve_default=True,
        ),
    ]
