# -*- coding: utf-8 -*-

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class SfsCompany(models.Model):
    """
    企業テーブル(m_company)
    """

    company_cd       = models.CharField(_(u'企業コード'), max_length=100, null=False, blank=False)
    company_name     = models.CharField(_(u'企業名称'), max_length=100, null=False, blank=False)
    money            = models.CharField(_(u'資本金'), max_length=100, null=False, blank=False)
    create_date      = models.DateField(_(u'成立日'), null=False, blank=False, default=timezone.now)
    manager_name     = models.CharField(_(u'代表取締役'), max_length=100, null=False, blank=False)
    sub_manager_name = models.CharField(_(u'取締役'), max_length=100, null=False, blank=False)
    address          = models.CharField(_(u'住所'), max_length=255, null=False, blank=False)
    email            = models.EmailField(_(u'メールアドレス'), max_length=100, null=False, blank=False)
    telphone         = models.CharField(_(u'電話'), max_length=20, null=False, blank=False)

    class Meta:
        app_label = 'sfs'
        db_table  = 'm_company'
        verbose_name = _(u'企業')
        verbose_name_plural = _(u'業務 : 企業 (%s)' % db_table)
        ordering = ['id', ]
