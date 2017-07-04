# -*- coding: utf-8 -*-

from django.db import models

from django.utils.translation import ugettext_lazy as _


class SfsCaption(models.Model):
    """
    項目タイトルマスタ(m_caption)
    """

    code     = models.CharField(_(u'コード'), max_length=20, null=False, blank=False,)
    title_jp = models.CharField(_(u'名称(ja)'), max_length=100, null=False, blank=False,)
    title_en = models.CharField(_(u'名称(en)'), max_length=100, null=True, blank=True,)
    title_th = models.CharField(_(u'名称(th)'), max_length=100, null=True, blank=True,)
    page_id  = models.PositiveIntegerField(_(u'画面ID'), null=True, blank=True, default=None,)

    def __str__(self):
        return u"%s=%s" % (self.code, self.title_jp)

    def __unicode__(self):  # Python 2
        return self.__str__()

    class Meta:
        app_label = 'sfs'
        db_table = 'm_caption'
        verbose_name = _(u'項目タイトル')
        verbose_name_plural = _(u'業務 : 項目タイトル (%s)' % db_table)
        ordering = ['id',]
