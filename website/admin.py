# -*- coding: utf-8 -*-

import logging

from django.contrib import admin

from .models import Place, Number, Subscription

logger = logging.getLogger(__name__)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (u'id', u'name', u'validation',)
    list_editable = (u'name', u'validation')
    row_id_fields = (u'name',)
    search_fields = (u'name',)


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = (u'number', u'timestamp', u'location', u'user',)
    list_filter = (u'location__name', u'user__username')
    list_select_related = (u'location', u'user')
    row_id_fields = (u'number',)
    search_fields = (u'number', u'location', u'user',)
    readonly_fields = (u'fingerprint',)
    date_hierarchy = u'timestamp'

    def has_change_permission(self, request, obj=None):
        result = super().has_change_permission(request, obj) and \
                 (not obj or (obj and request.user.is_superuser) or (obj.user == request.user))
        return result

    def get_queryset(self, request):
        result = super().get_queryset(request)
        if request.user.is_superuser:
            return result

        return result.filter(user=request.user)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (u'id', u'number', u'phone', u'email', u'telegram', u'last_notify')
    search_fields = (u'number',)
