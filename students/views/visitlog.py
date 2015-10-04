# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from .students import students_list
from ..models import Student

# Views for Visitlog
def visit_log(request):
    student_log = Student.objects.all()

    days = (
        {'week_day': u'Пн',
        'day':1},
        {'week_day': u'Вт',
        'day':2},
        {'week_day': u'Ср',
        'day':3},
        {'week_day': u'Чт',
        'day':4},
        {'week_day': u'Пт',
        'day':5},
        {'week_day': u'Сб',
        'day':6},
        {'week_day': u'Нд',
        'day':7},
        {'week_day': u'Пн',
        'day':8},
        {'week_day': u'Вт',
        'day':9},
        {'week_day': u'Ср',
        'day':10},
        {'week_day': u'Чт',
        'day':11},
        {'week_day': u'Пт',
        'day':12},
        {'week_day': u'Сб',
        'day':13},
        {'week_day': u'Нд',
        'day':14},
        {'week_day': u'Пн',
        'day':15},
        {'week_day': u'Вт',
        'day':16},
        {'week_day': u'Ср',
        'day':17},
        {'week_day': u'Чт',
        'day':18},
        {'week_day': u'Пт',
        'day':19},
        {'week_day': u'Сб',
        'day':20},
        {'week_day': u'Нд',
        'day':21},
        {'week_day': u'Пн',
        'day':22},
        {'week_day': u'Сб',
        'day':23},
        {'week_day': u'Нд',
        'day':24},
        {'week_day': u'Пн',
        'day':25},
        {'week_day': u'Вт',
        'day':26},
        {'week_day': u'Ср',
        'day':27},
        {'week_day': u'Чт',
        'day':28},
        {'week_day': u'Пт',
        'day':29},
        {'week_day': u'Сб',
        'day':30},
        {'week_day': u'Нд',
        'day':31},
        )
    return render(request, 'students/visit_log.html', {'student_log': student_log, 'days': days})


def visit_student(request, sid):
    return HttpResponse('<h1>Student visiting log %s</h1>' % sid)

def visitlog_update(request):
    return HttpResponse('<h1>Visitlog update</h1>')
