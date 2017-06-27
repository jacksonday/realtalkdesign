# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View, FormView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from ..newsletter.forms import JoinForm

# class HomeView(View):
# 	def get(self, request, *args, **kwargs):
# 		return render(request, "landingpages/home.html", {})

class HomeView(CreateView):
	template_name = 'landingpages/home.html'
	form_class = JoinForm
	success_url = '/'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context['object'] = Page.objects.filter(featured=True).first() #.order_by("?").first()
		return context

	def get_success_message(self, cleaned_data):
		print(cleaned_data)
		return "Thank you for joining!"