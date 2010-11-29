from django.conf import settings
from django.contrib import admin
from django import forms

from planet import models as planet_models

from models import *

class FanzinePartPostInline(admin.StackedInline):
    model = FanzinePartPost
    raw_id_fields = (
        'post',
    )

class FanzinePartAdminForm(forms.ModelForm):
    model = FanzinePart

    class Media:
        js = (
            settings.STATIC_URL + 'js/jquery-1.4.2.min.js',
            settings.STATIC_URL + 'js/jquery-ui-1.8.6.fanzine.min.js',
            settings.STATIC_URL + 'js/menu-sort.js',
        )

class FanzinePartAdmin(admin.ModelAdmin):
    form = FanzinePartAdminForm
    list_display = (
        'pk',
        'fanzine',
        'tag',
        'text',
    )
    list_display_links = (
        'pk',
    )
    search_fields = (
        'text',
    )
    list_filter = (
        'fanzine',
    )
    inlines = (
        FanzinePartPostInline,
    )
    raw_id_fields = (
        'tag',
        'fanzine',
    )


class FanzinePartInline(admin.StackedInline):
    model = FanzinePart
    raw_id_fields = (
        'tag',
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
        'id',
        'date',
        'title',
        'slug',
        'text',
    )
    list_display_links = (
        'id',
    )
    search_fields = (
        'title',
        'text',
    )
    list_filter = (
        'date',
    )
    list_editable = (
        'date',
        'title',
        'slug',
        'text',
    )
    inlines = (
        FanzinePartInline,
    )

admin.site.register(Fanzine, FanzineAdmin)
admin.site.register(FanzinePart, FanzinePartAdmin)
