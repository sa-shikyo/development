# -*- coding: utf-8 -*-

import datetime

from datetime import date

from django.views.decorators.http import require_http_methods
from django.shortcuts import render

from sfs.models import SfsManagermsg
from sfs.models import SfsTopic
from sfs.models import SfsCompany
from sfs.models import SfsIdea
from sfs.models import SfsBusiness


@require_http_methods(["GET", "POST"])
def sfs_homepage(request):
    """
    ホームページ
    """

    # ------------------------
    # 管理者のメッセージの取得
    # ------------------------
    # today = date.today()
    managermsg = SfsManagermsg.objects.filter().first()

    # ------------------
    # トピック情報の取得
    # ------------------
    topic = SfsTopic.objects.filter().all()

    return render(request, 'sfs/homepage.html', {
        'managermsg': managermsg,
        'topic': topic,
    })


@require_http_methods(["GET", "POST"])
def sfs_company_message(request):
    """
    社会情報
    """

    # --------------
    # 社会情報の取得
    # --------------
    company_info = SfsCompany.objects.filter().first()

    return render(request, 'sfs/company_message.html', {
        'company_info': company_info,
    })


@require_http_methods(["GET", "POST"])
def sfs_company_idea(request):
    """
    社会理念
    """

    # --------------
    # 社会理念の取得
    # --------------
    idea = SfsIdea.objects.filter().first()

    return render(request, 'sfs/company_idea.html', {
        'idea': idea,
    })


@require_http_methods(["GET", "POST"])
def sfs_company_business(request):
    """
    業務内容
    """

    # --------------
    # 業務内容の取得
    # --------------
    business = SfsBusiness.objects.filter().first()

    return render(request, 'sfs/company_business.html', {
        'business': business,
    })


@require_http_methods(["GET", "POST"])
def sfs_company_employment(request):
    return render(request, 'sfs/company_employment.html', {})
