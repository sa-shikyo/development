# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SfsAccount',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=255, verbose_name='メールアドレス')),
                ('user_name', models.CharField(max_length=100, verbose_name='ユーザー名')),
                ('apply_begin', models.DateField(default=django.utils.timezone.now, verbose_name='適用開始日')),
                ('apply_end', models.DateField(default='9999-12-31', verbose_name='適用開始日')),
                ('create_date', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
            options={
                'db_table': 'm_account',
                'verbose_name': 'アカウント',
                'verbose_name_plural': '業務 : アカウント (m_account)',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SfsManagermsg',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='内容')),
                ('apply_begin', models.DateField(verbose_name='適用開始日')),
                ('apply_end', models.DateField(verbose_name='適用終了日')),
                ('create_user', models.CharField(max_length=100, verbose_name='作成者')),
                ('create_date', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
            options={
                'db_table': 'm_managermsg',
                'verbose_name': '管理者のメッセージ',
                'verbose_name_plural': '業務 : 管理者のメッセージ (m_managermsg)',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SfsTopic',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='トッピク内容')),
                ('apply_begin', models.DateField(default=django.utils.timezone.now, verbose_name='適用開始日')),
                ('create_user', models.CharField(max_length=100, verbose_name='作成者')),
                ('create_date', models.DateField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
            options={
                'db_table': 'm_topic',
                'verbose_name': 'トッピク',
                'verbose_name_plural': '業務 : トッピク (m_topic)',
                'ordering': ['-id'],
            },
        ),
    ]
