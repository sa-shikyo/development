# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfs', '0002_sfsbusiness_sfscompany_sfsemployment_sfsidea'),
    ]

    operations = [
        migrations.CreateModel(
            name='SfsCaption',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('code', models.CharField(max_length=20, verbose_name='コード')),
                ('title_jp', models.CharField(max_length=100, verbose_name='名称(ja)')),
                ('title_en', models.CharField(max_length=100, null=True, blank=True, verbose_name='名称(en)')),
                ('title_th', models.CharField(max_length=100, null=True, blank=True, verbose_name='名称(th)')),
                ('page_id', models.PositiveIntegerField(default=None, null=True, verbose_name='画面ID')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': '業務 : 項目タイトル (m_caption)',
                'verbose_name': '項目タイトル',
                'db_table': 'm_caption',
            },
        ),
        migrations.AlterModelOptions(
            name='sfscompany',
            options={'ordering': ['id'], 'verbose_name_plural': '業務 : 企業 (m_company)', 'verbose_name': '企業'},
        ),
    ]
