# -*- coding: utf-8 -*-

import datetime

from datetime import date

from django.views.decorators.http import require_http_methods
from django.shortcuts import render

from sfs.models import SfsManagermsg


@require_http_methods(["GET", "POST"])
def sfs_homepage(request):
    today = date.today()
    managermsg = SfsManagermsg.object.filter(apply_begin=<today).first()
    return render(request, 'sfs/homepage.html', {'managermsg': managermsg,})


@require_http_methods(["GET", "POST"])
def sfs_company_message(request):
    return render(request,'sfs/company_message.html', {})


@require_http_methods(["GET", "POST"])
def sfs_company_idea(request):
    return render(request,'sfs/company_idea.html', {})


@require_http_methods(["GET", "POST"])
def sfs_company_business(request):
    return render(request,'sfs/company_business.html', {})


@require_http_methods(["GET", "POST"])
def sfs_company_employment(request):
    return render(request,'sfs/company_employment.html', {})
