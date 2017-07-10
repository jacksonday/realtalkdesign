# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View, FormView, CreateView

from django.contrib.messages.views import SuccessMessageMixin

from ..newsletter.forms import RevJoinForm, SubJoinForm

# class HomeView(View):
# 	def get(self, request, *args, **kwargs):
# 		return render(request, "landingpages/home.html", {})

class HomeView(SuccessMessageMixin, CreateView):
	template_name = 'landingpages/home.html'
	form_classes = [RevJoinForm, SubJoinForm]
	success_url = '/'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})
	# def get_context_data(self, *args, **kwargs):
	# 	context = super(HomeView, self).get_context_data(*args, **kwargs)
	# 	context['object'] = Pages.objects.filter(featured=True).first() #.order_by("?").first()
 # 		return context
	def get_success_message(self, cleaned_data):
		print(cleaned_data)
		return "Thank you for joining!"

def home(request):
	template = 'landingpages/home.html'
	r_form = RevJoinForm
	s_form = SubJoinForm
	return render(request, template)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
# Remove above when finished
#
#
