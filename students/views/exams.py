# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from ..models import Exam
from ..util import paginate

# Views for exams
def exams_list(request):
    exams = Exam.objects.all()

    # try to order exams list
    order_by = request.GET.get('order_by', '')
    if order_by in ('course', 'lecturer', 'exam_group', 'exam_date'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    # paginate exams
    context = paginate(exams, 3, request, {}, var_name='exams')

    return render(request, 'students/exams_list.html', context)

def exams_add(request):
    return HttpResponse('<h1>Exam Add Form</h1>')

def exams_edit(request, gid):
    return HttpResponse('<h1>Edit Exam %s</h1>' % gid)

def exams_delete(request, gid):
    return HttpResponse('<h1>Delete Exam %s</h1>' % gid)
