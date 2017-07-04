# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sfs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SfsBusiness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='内容')),
                ('apply_begin', models.DateField(verbose_name='適用開始日')),
                ('apply_end', models.DateField(verbose_name='適用終了日')),
                ('create_user', models.CharField(verbose_name='作成者', max_length=100)),
                ('create_date', models.DateField(verbose_name='作成日', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '業務',
                'db_table': 'm_business',
                'verbose_name_plural': '業務 : 業務 (m_business)',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SfsCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('company_cd', models.CharField(verbose_name='企業コード', max_length=100)),
                ('company_name', models.CharField(verbose_name='企業名称', max_length=100)),
                ('money', models.CharField(verbose_name='資本金', max_length=100)),
                ('create_date', models.DateField(verbose_name='成立日', default=django.utils.timezone.now)),
                ('manager_name', models.CharField(verbose_name='代表取締役', max_length=100)),
                ('sub_manager_name', models.CharField(verbose_name='取締役', max_length=100)),
                ('address', models.CharField(verbose_name='住所', max_length=255)),
                ('email', models.EmailField(verbose_name='メールアドレス', max_length=100)),
                ('telphone', models.CharField(verbose_name='電話', max_length=20)),
            ],
            options={
                'verbose_name': '企業',
                'db_table': 'm_company',
                'verbose_name_plural': '業務 : 企業 (m_company)',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SfsEmployment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='内容')),
                ('apply_begin', models.DateField(verbose_name='適用開始日')),
                ('apply_end', models.DateField(verbose_name='適用終了日')),
                ('create_user', models.CharField(verbose_name='作成者', max_length=100)),
                ('create_date', models.DateField(verbose_name='作成日', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '採用',
                'db_table': 'm_employment',
                'verbose_name_plural': '業務 : 採用 (m_employment)',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SfsIdea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='内容')),
                ('apply_begin', models.DateField(verbose_name='適用開始日')),
                ('apply_end', models.DateField(verbose_name='適用終了日')),
                ('create_user', models.CharField(verbose_name='作成者', max_length=100)),
                ('create_date', models.DateField(verbose_name='作成日', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '理念',
                'db_table': 'm_idea',
                'verbose_name_plural': '業務 : 理念 (m_idea)',
                'ordering': ['-id'],
            },
        ),
    ]
