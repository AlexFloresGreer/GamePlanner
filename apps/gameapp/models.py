from __future__ import unicode_literals
from django.db import models
import re
from django.contrib import messages
import bcrypt
from datetime import datetime, date, timedelta, time
from time import strftime
# Create your models here.

class Game(models.Model):
	game = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	players = models.CharField(max_length=100)
	date = models.DateField()
	time = models.TimeField()
	game_starter = models.ForeignKey('loginreg.User', related_name="usersstarts")
	game_joiner = models.ManyToManyField('loginreg.User', related_name="jointrip")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)