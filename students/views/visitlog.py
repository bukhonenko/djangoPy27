# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Views for Students
def visit_log(request):
    return render(request, 'students/visit_log.html', {})

def visit_student(request, sid):
    return HttpResponse('<h1>Student visiting log %s</h1>' % sid)

def visitlog_update(request):
    return HttpResponse('<h1>Visitlog update</h1>')
