# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Views for Students
def visit_log(request):
    return HttpResponse('<h1>Students Visitlog</h1>')
