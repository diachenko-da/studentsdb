# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def groups_list(request):
	students = (
		{'id': 1,
		'first_name': u'Дмитро',
		'last_name': u'Дяченко',
		'group': u'КСД-21',
		'ticket': 21,
		'image': 'img/beavis-2.png'},
		{'id': 2,
		'first_name': u'Анатолій',
		'last_name': u'Кустливий',
		'group': u'КСД-22',
		'ticket': 27,
		'image': 'img/bart.jpg'},
		{'id': 3,
		'first_name': u'Микола',
		'last_name': u'Кустливий',
		'group': u'КСД-23',
		'ticket': 28,
		'image': 'img/butthead.jpg'},
		)
	return render(request, 'students/groups_list.html', {'students': students})

def groups_add(request):
	return HttpResponse('<h1>Groups Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)