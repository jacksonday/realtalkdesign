# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class RevJoin(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email

class SubJoin(models.Model):
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email