# -*- coding: utf-8 -*-

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class SFS_NOTICE(models.Model):
    """
    お知らせテーブル
    """

    content = models.TextField(_(u'お知らせ内容'), null=False, blank=False)
    user    = models.CharField(_(u'作成者'), max_length=100, null=False, blank=False)
    date    = models.DateField(_(u'お知らせ日'), null=False, blank=False, default=timezone.now)

    class Meta:
        app_label = 'sfs'
        db_table  = 'm_notice'
