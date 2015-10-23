# -*- coding: utf-8 -*-

import re
from django.core.urlresolvers import resolve
from django.template.defaulttags import register


@register.simple_tag
def active(request, pattern):
    return 'active' if re.search(pattern, request.path) else ''


@register.simple_tag()
def get_current_view(request):
    return resolve(request.path).view_name
