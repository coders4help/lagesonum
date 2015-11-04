# -*- coding: utf-8 -*-

import logging

from django.contrib import admin
from django.db.models import Q

from .models import Place, Number, Holiday

logger = logging.getLogger(__name__)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (u'id', u'name', u'validation',)
    list_editable = (u'name', u'validation')
    row_id_fields = (u'name',)
    search_fields = (u'name',)


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = (u'number', u'location', u'appointment', u'incomplete')
    list_filter = (u'location__name', u'user__username', u'incomplete', u'appointment')
    list_select_related = (u'location', u'user')
    row_id_fields = (u'number',)
    search_fields = (u'number', u'location', u'user', u'appointment')
    # inlines = (u'incomplete',)

    def has_change_permission(self, request, obj=None):
        result = super().has_change_permission(request, obj) and \
                 (not obj or (obj and request.user.is_superuser) or (obj.user == request.user))
        return result

    def get_queryset(self, request):
        result = super().get_queryset(request)
        if request.user.is_superuser:
            return result

        user_filter = Q(user=request.user).add(Q(location__name__in=[g.name for g in request.user.groups.all()]), Q.OR)
        return result.filter(user_filter)


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = (u'location', u'date')
    list_filter = (u'location__name',)
    list_display_links = (u'date',)

    def get_queryset(self, request):
        result = super().get_queryset(request)
        if request.user.is_superuser:
            return result

        try:
            return result.filter(location__name__in=[g.name for g in request.user.groups.all()])
        except:
            pass

        return Holiday.objects.none()
