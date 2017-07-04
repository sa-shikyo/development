# -*- coding: utf-8 -*-

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class SfsIdea(models.Model):
    """
    理念テーブル(m_idea)
    """

    content     = models.TextField(_(u'内容'), null=False, blank=False)
    apply_begin = models.DateField(_(u'適用開始日'), null=False, blank=False)
    apply_end   = models.DateField(_(u'適用終了日'), null=False, blank=False)
    create_user = models.CharField(_(u'作成者'), max_length=100, null=False, blank=False)
    create_date = models.DateField(_(u'作成日'), null=False, blank=False, default=timezone.now)

    class Meta:
        app_label = 'sfs'
        db_table  = 'm_idea'
        verbose_name = _(u'理念')
        verbose_name_plural = _(u'業務 : 理念 (%s)' % db_table)
        ordering = ['-id', ]
