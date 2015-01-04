# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0007_auto_20141227_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holdingtypeproportionrule',
            name='percent',
            field=models.DecimalField(max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]
