# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=11, decimal_places=2)),
                ('purchase_date', models.DateField()),
                ('holding', models.ForeignKey(to='track.HoldingType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='holdingtype',
            name='minimum_holding_period',
            field=models.IntegerField(default=30),
            preserve_default=False,
        ),
    ]
