# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models
from django.forms import Select
from django.forms import TextInput
from django.forms import Textarea
from django.template.defaultfilters import linebreaksbr
from django.template.defaultfilters import truncatechars
from django.utils.html import escape


class ProjectModelAdmin(admin.ModelAdmin):
    """
    Base ModelAdmin
    """
    list_per_page = 20
    from netfields import CidrAddressField
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '60'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 8, 'cols': 80})},
        CidrAddressField: {'widget': TextInput(attrs={'size': '60',})},
    }

    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        サンプル：
            display_as_textarea = ['title_jp',]
        """
        formfield = super(ProjectModelAdmin, self).formfield_for_dbfield(db_field, **kwargs)

        display_as_textinput = getattr(self, 'display_as_textinput', [])
        display_as_textarea  = getattr(self, 'display_as_textarea', [])
        display_as_select    = getattr(self, 'display_as_select', [])

        if db_field.name in display_as_textinput:
            formfield.widget = TextInput(attrs=formfield.widget.attrs)
        elif db_field.name in display_as_textarea:
            formfield.widget = Textarea(attrs={'rows': 8, 'cols': 80})
        elif db_field.name in display_as_select:
            formfield.widget = Select(attrs=formfield.widget.attrs, choices=formfield.choices)

        return formfield

    @staticmethod
    def show_return_text(text, truncate=False):
        summary = escape(text)  # format_html("<u>{}</u>", xxx)
        if truncate:
            summary = truncatechars(summary, 40)
        summary = linebreaksbr(summary)  # 改行変換
        summary = summary.replace("<br />", u"<b><font color='red'>&crarr;</font></b><br />")
        return summary

        # class Media:
        #     css = {
        #         # <link href="/static/my_styles.css" type="text/css" media="all" rel="stylesheet" />
        #         "all": ("my_styles.css",)
        #     }
        #     js = (
        #         # <script type="text/javascript" src="/static/my_code.js"></script>
        #         "my_code.js",
        #     )
