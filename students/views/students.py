# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def students_list(request):
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
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)