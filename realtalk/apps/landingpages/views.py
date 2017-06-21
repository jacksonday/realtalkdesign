# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View, FormView, CreateView

from ..newsletter.forms import JoinForm

# class HomeView(View):
# 	def get(self, request, *args, **kwargs):
# 		return render(request, "landingpages/home.html", {})

class HomeView(CreateView):
	template_name = 'landingpages/home.html'
	form_class = JoinForm
	success_url = '/'