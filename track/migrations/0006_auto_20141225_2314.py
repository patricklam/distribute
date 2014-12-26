# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0005_auto_20141225_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoldingLocationRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField()),
                ('account_type', models.CharField(max_length=2, choices=[(b'RRSP', b'RRSP'), (b'TFSA', b'TFSA'), (b'NR', b'NR')])),
                ('holding_type', models.ForeignKey(to='track.HoldingType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='HoldingRule',
            new_name='HoldingTypeProportionRule',
        ),
        migrations.RemoveField(
            model_name='accountlocationrule',
            name='holding_type',
        ),
        migrations.DeleteModel(
            name='AccountLocationRule',
        ),
    ]
