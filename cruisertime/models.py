from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Meetup(models.Model):
    meet_date = models.DateField(auto_now=False, auto_now_add=False)
    meet_time = models.TimeField(auto_now=False, auto_now_add=False)
    lift_name = models.CharField(max_length=200)
    lift_terminal = models.CharField(max_length=200)
    notes_text = models.CharField(max_length=200)
    meet_name = models.CharField(max_length=200, default='Test')	
    def __str__(self):
        return self.meet_name

