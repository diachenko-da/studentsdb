# -*- coding: utf-8 -*-

from django.db import models
from groups import Group

class Exam(models.Model):
	"""Exam Model - Модель заліків"""
	class Meta(object):
		verbose_name=u'Екзамен'
		verbose_name_plural=u'Екзамени'

	subject = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u'Предмет')

	group = models.OneToOneField('Group',
		verbose_name=u'Група',
		blank=False,
		null=False)

	teacher = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u'Викладач')

	date = models.DateField(
		blank=False,
		verbose_name=u'Дата',
		null=False)

	def __unicode__(self):
		return u'{} {}'.format(self.subject, self.date)