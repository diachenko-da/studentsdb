from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG

urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'students.views.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students_add', name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', 'students.views.students_edit', name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students_delete', name='students_delete'),

    # Groups urls
    url(r'^groups/$', 'students.views.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups_add', name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups_edit', name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups_delete', name='groups_delete'),
    
    # Journal url
    url(r'^journal/', 'students.views.journal', name='journal'),
    
    # Exam url
    url(r'^exams/$', 'students.views.exams_list', name='exams'),
    url(r'^exams/add/$', 'students.views.exams_add', name='exams_add'),
    url(r'^exams/(?P<eid>\d+)/edit/$', 'students.views.exams_edit', name='exams_edit'),
    url(r'^exams/(?P<eid>\d+)/delete/$', 'students.views.exams_delete', name='exams_delete'),

    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('', url(r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}))