# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, DeleteView, CreateView
from django.db.models.deletion import ProtectedError

from ..models import Group
from ..util import paginate

# Views for Groups
def groups_list(request):
    groups = Group.objects.all()

    # try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # paginate groups
    context = paginate(groups, 3, request, {}, var_name='groups')

    return render(request, 'students/groups_list.html', context)

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

# def groups_delete(request, gid):
#     return HttpResponse('<h1>Delete Group %s</h1>' % gid)

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message= Групу успішно видалено!' % reverse('home')

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)

        except ProtectedError:
            return HttpResponseRedirect(u'%s?status_message=Група не може бути видалена зараз!'% reverse('groups'))
