# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Views for Groups
def groups_list(request):
    groups = (
        {'id': 1,
        'group_title': u'МтМ-27',
        'group_leader': u'Дарт Вейдер',},
        {'id': 2,
        'group_title': u'МтМ-28',
        'group_leader': u'Майстер Йода',},
        {'id': 3,
        'group_title': u'МтМ-29',
        'group_leader': u'Джабба Хатт',},
        )
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
