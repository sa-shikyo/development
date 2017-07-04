# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfs', '0003_auto_20170704_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sfscaption',
            name='page_id',
            field=models.PositiveIntegerField(default=None, blank=True, null=True, verbose_name='画面ID'),
        ),
    ]
