from __future__ import unicode_literals

import redis

from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from django.urls import reverse
from six import python_2_unicode_compatible
from timezone_field import TimeZoneField

import arrow

@python_2_unicode_compatible
class Appointment(models.Model):
    name = models.Charfield(max_length=150)
    phone_number = models.Charfield(max_length=15)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='UTC')

    # Not visible for users
    task_id = models.Charfield(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Appointment #{0} - {1}'.format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('reminders:view_appointment', args=[str(self.id)])
