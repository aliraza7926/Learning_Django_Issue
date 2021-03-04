from django.shortcuts import render
from django.views.generic import TemplateView

class IssuView(TemplateView):
    template_name ='test.html'

