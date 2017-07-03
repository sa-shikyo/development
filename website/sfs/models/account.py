# -*- coding: utf-8 -*-

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class SFS_ACCOUNT(models.Model):
    """
    ユーザーテーブル
    """

    email       = models.EmailField(_(u'メールアドレス'), max_length=255, null=False, blank=False)
    user_name   = models.CharField(_(u'ユーザー名'), max_length=100, null=False, blank=False)
    apply_begin = models.DateField(_(u'適用開始日'), null=False, blank=False, default=timezone.now)
    apply_end   = models.DateField(_(u'適用開始日'), null=False, blank=False, default='9999-12-31')
    create_date = models.DateField(_(u'作成日'), null=False, blank=False, default=timezone.now)

    class Meta:
        app_label = 'sfs'
        db_table  = 'm_account'
        verbose_name = _(u'アカウント')
        verbose_name_plural = _(u'業務 : アカウント (%s)' % db_table)
        ordering = ['-id', ]
