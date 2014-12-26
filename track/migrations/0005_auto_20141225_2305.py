# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0004_auto_20141225_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountLocationRule',
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
            old_name='AllocationRule',
            new_name='HoldingRule',
        ),
        migrations.RemoveField(
            model_name='locationrule',
            name='holding_type',
        ),
        migrations.DeleteModel(
            name='LocationRule',
        ),
    ]
