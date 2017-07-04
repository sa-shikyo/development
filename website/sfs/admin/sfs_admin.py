# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from sfs.models import SfsAccount
from sfs.models import SfsManagermsg
from sfs.models import SfsTopic
from sfs.models import SfsCompany
from sfs.models import SfsIdea
from sfs.models import SfsBusiness
from sfs.models import SfsEmployment
from sfs.models import SfsCaption


admin.site.unregister(Group)
admin.site.unregister(User)

# admin.site.register(SfsAccount)
class SfsAccountAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'email', 'user_name', 'apply_begin', 'apply_end', 'create_date',
    )
    ordering = ('-id',)
    pass
admin.site.register(SfsAccount, SfsAccountAdmin)

# @admin.register(SfsAccount)
# class SfsAccountAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'email', 'user_name', 'apply_begin', 'apply_end', 'create_date',
#     )
#     ordering = ('id',)
#     pass

# admin.site.register(SfsManagermsg)
class SfsManagermsgAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'content', 'apply_begin', 'apply_end', 'create_user', 'create_date',
    )
    ordering = ('-id',)
    pass
admin.site.register(SfsManagermsg, SfsManagermsgAdmin)

# admin.site.register(SfsTopic)
class SfsTopicAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'content', 'apply_begin', 'create_user', 'create_date',
    )
    ordering = ('-id',)
    pass
admin.site.register(SfsTopic, SfsTopicAdmin)

# admin.site.register(SfsCompany)
class SfsCompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'company_cd', 'company_name', 'money', 'create_date', 'manager_name', 'sub_manager_name', 'address', 'email', 'telphone',
    )
    ordering = ('id',)
    pass
admin.site.register(SfsCompany, SfsCompanyAdmin)

# admin.site.register(SfsIdea)
class SfsIdeaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'content', 'apply_begin', 'apply_end', 'create_user', 'create_date',
    )
    ordering = ('-id',)
    pass
admin.site.register(SfsIdea, SfsIdeaAdmin)

# admin.site.register(SfsBusiness)
class SfsBusinessAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'content', 'apply_begin', 'apply_end', 'create_user', 'create_date',
    )
    ordering = ('-id',)
    pass
admin.site.register(SfsBusiness, SfsBusinessAdmin)

# admin.site.register(SfsEmployment)
class SfsEmploymentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'content', 'apply_begin', 'apply_end', 'create_user', 'create_date',
    )
    ordering = ('-id',)
    pass
admin.site.register(SfsEmployment, SfsEmploymentAdmin)

# admin.site.register(SfsCaption)
class SfsCaptionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'code', 'title_jp', 'title_en', 'title_th', 'page_id',
    )
    ordering = ('id',)
    pass
admin.site.register(SfsCaption, SfsCaptionAdmin)

admin.site.register(Session)
