# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# from .students import students_list
from ..models import Student

class JournalView(TemplateView):
    template_name = 'students/visit_log.html'


def visit_student(request, sid):
    return HttpResponse('<h1>Student visiting log %s</h1>' % sid)

def visitlog_update(request):
    return HttpResponse('<h1>Visitlog update</h1>')
