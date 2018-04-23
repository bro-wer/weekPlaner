from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView

# Create your views here.
app_name='calendarManager'


class HomePage(TemplateView):

    template_name = "calendarManager/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context