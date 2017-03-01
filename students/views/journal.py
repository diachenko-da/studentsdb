# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from ..models import Student

def journal(request):
	students = Student.objects.all()
	return render(request, 'students/journal.html', {'students': students})