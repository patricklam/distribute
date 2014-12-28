# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0006_auto_20141225_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holdinglocationrule',
            name='account_type',
            field=models.CharField(max_length=4, choices=[(b'RRSP', b'RRSP'), (b'TFSA', b'TFSA'), (b'NR', b'NR')]),
            preserve_default=True,
        ),
    ]
