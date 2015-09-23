# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Views for Students
def students_list(request):
    students = (
        {'id': 1,
        'first_name': u'Олександр',
        'last_name': u'Ройтбурд',
        'ticket': 2135,
        'image': 'img/roi.jpg'},
        {'id': 2,
        'first_name': u'Орест',
        'last_name': u'Лютий',
        'ticket': 2123,
        'image': 'img/roi1.jpg'},
        {'id': 3,
        'first_name': u'Дмитро',
        'last_name': u'Ярош',
        'ticket': 2199,
        'image': 'img/roi2.jpg'},
        )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
