# -*- coding: utf-8 -*-

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class SFS_MANAGERMSG(models.Model):
    """
    管理者メッセージテーブル
    """

    content     = models.TextField(_(u'内容'), null=False, blank=False)
    create_user = models.CharField(_(u'作成者'), max_length=100, null=False, blank=False)
    create_date = models.DateField(_(u'作成日'), null=False, blank=False, default=timezone.now)

    class Meta:
        app_label = 'sfs'
        db_table  = 'm_managermsg'
