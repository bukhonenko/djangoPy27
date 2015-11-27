"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

from students.views.students import StudentUpdateView, StudentDeleteView, StudentCreateView
from students.views.groups import GroupDeleteView
from students.views.contact_admin import ContactView
from students.views.visitlog import JournalView

urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', StudentCreateView.as_view(), name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

    # Groups urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups.groups_add', name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$','students.views.groups.groups_edit', name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='groups_delete'),

    # Visitlog urls
    url(r'^visitlog/(?P<pk>\d+)?/?$', JournalView.as_view(), name='visitlog'),
    url(r'^visitlog/(?P<sid>\d+)/$', 'students.views.visitlog.visit_student', name='visit_student'),
    url(r'^visitlog/update/$', 'students.views.visitlog.visitlog_update', name='visitlog_update'),

    # Exams urls
    url(r'^exams/$', 'students.views.exams.exams_list', name='exams'),
    url(r'^exams/add/$', 'students.views.exams.exams_add', name='exams_add'),
    url(r'^exams/(?P<gid>\d+)/edit/$','students.views.exams.exams_edit', name='exams_edit'),
    url(r'^exams/(?P<gid>\d+)/delete/$','students.views.exams.exams_delete', name='exams_delete'),

    # Contact Admin Form
    url(r'^contact-admin/$', ContactView.as_view(), name='contact_admin'),
    #  url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin'),


    url(r'^admin/', include(admin.site.urls)),
    )
from .settings import MEDIA_ROOT, DEBUG
if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': MEDIA_ROOT}))
