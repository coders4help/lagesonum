# -*- coding: utf-8 -*-
from datetime import date, timedelta

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

import re


class Place(models.Model):

    description = u'A place numbers are shown at and for'

    name = models.CharField(max_length=20, unique=True, verbose_name=_('place'))
    validation = models.CharField(max_length=256, verbose_name=_('pattern'))
    validation_msg = models.CharField(max_length=256, verbose_name=_('pattern message'))
    release_date = models.DateField(default=date.today() + timedelta(days=1), verbose_name=_('release date'))
    per_day_incomplete = models.PositiveIntegerField(verbose_name=_('incomplete cases per day'))
    per_day_missed = models.PositiveIntegerField(verbose_name=_('missed appointments per day'))

    class Meta:
        verbose_name = _('place')
        verbose_name_plural = _('places')

    def validate(self, value):
        if self.validation:
            return re.match(self.validation, value)
        return None

    def __str__(self):
        return u'{}'.format(self.name)

    def __repr__(self):
        return u'{} ({})'.format(self.name, self.validation)


class Number(models.Model):

    description = u'A number shown at a place and entered into dataset'

    number = models.CharField(max_length=30, unique=True, verbose_name=_('number'))
    timestamp = models.DateTimeField(default=now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='+', on_delete=models.SET_NULL)
    location = models.ForeignKey('Place', on_delete=models.PROTECT)

    appointment = models.DateField(null=True, blank=True, db_index=True, verbose_name=_('appointment'))
    incomplete = models.BooleanField(default=False, db_index=True, verbose_name=_('incomplete registration'))

    class Meta:
        verbose_name = _('number')
        verbose_name_plural = _('numbers')

    def __str__(self):
        return '{}@{} (Timestamp: {}; Incomplete: {}; Appointment: {})'\
            .format(self.number, self.location, self.timestamp, self.incomplete, self.appointment)


class Holiday(models.Model):

    description = u'Weekdays not work is done'

    location = models.ForeignKey('Place', on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, db_index=True, verbose_name=_('dayoff'))

    class Meta:
        verbose_name = _('holiday')
        verbose_name_plural = _('holidays')

    def __str__(self):
        return '{}@{}'.format(self.date, self.location)
