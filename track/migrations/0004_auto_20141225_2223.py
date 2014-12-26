# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_auto_20141225_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(max_length=4, choices=[(b'RRSP', b'RRSP'), (b'TFSA', b'TFSA'), (b'NR', b'NR')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='locationrule',
            name='account_type',
            field=models.CharField(max_length=2, choices=[(b'RRSP', b'RRSP'), (b'TFSA', b'TFSA'), (b'NR', b'NR')]),
            preserve_default=True,
        ),
    ]
