# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "landingpages/home.html", {})
