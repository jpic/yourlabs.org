from django.conf import settings
from django.contrib import admin
from django import forms

from planet import models as planet_models

from models import *

class FanzinePostInline(admin.StackedInline):
    model = FanzinePost
    raw_id_fields = (
        'post',
    )

class FanzineAdminForm(forms.ModelForm):
    model = Fanzine

    class Media:
        js = (
            settings.STATIC_URL + 'js/jquery-1.4.2.min.js',
            settings.STATIC_URL + 'js/jquery-ui-1.8.6.fanzine.min.js',
            settings.STATIC_URL + 'js/menu-sort.js',
        )

class FanzineAdmin(admin.ModelAdmin):
    form = FanzineAdminForm
    list_display = (
        'date',
        'editorial_author',
        'title',
        'editorial',
    )
    list_display_links = (
        'title',
    )
    search_fields = (
        'title',
        'editorial',
    )
    list_filter = (
        'date',
    )
    list_editable = (
        'date',
    )
    inlines = (
        FanzinePostInline,
    )

admin.site.register(Fanzine, FanzineAdmin)
