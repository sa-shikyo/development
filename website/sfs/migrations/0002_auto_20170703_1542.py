# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sfs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sfs_account',
            options={'verbose_name': 'アカウント', 'ordering': ['-id'], 'verbose_name_plural': '業務 : アカウント (m_account)'},
        ),
        migrations.AlterModelOptions(
            name='sfs_managermsg',
            options={'verbose_name': '管理者メッセージ', 'ordering': ['-id'], 'verbose_name_plural': '業務 : 管理者メッセージ (m_managermsg)'},
        ),
        migrations.AlterModelOptions(
            name='sfs_notice',
            options={'verbose_name': 'お知らせ', 'ordering': ['-id'], 'verbose_name_plural': '業務 : お知らせ (m_notice)'},
        ),
    ]
