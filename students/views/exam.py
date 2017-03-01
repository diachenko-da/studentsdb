# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Exam

def exams_list(request):
	exam = Exam.objects.all()
	return render(request, 'students/exam.html', {'students' : exam})

def exams_add(request):
	return HttpResponse('<h1>Exam Add Form</h1>')

def exams_edit(request, eid):
	return HttpResponse('<h1>Exam Edit %s</h1>' % eid)

def exams_delete(request, eid):
	return HttpResponse('<h1>Exam Delete %s</h1>' % eid)