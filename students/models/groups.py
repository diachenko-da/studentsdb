# -*- coding: utf-8 -*-

from django.db import models
from students import Student

class Group(models.Model):
	"""Group Model - Модель Групи"""

	class Meta(object):
		verbose_name = u"Група"
		verbose_name_plural = u"Групи"

	title = models.CharField(
		max_length=256,
		blank=False,
		verbose_name=u"Назва")

	leader = models.OneToOneField('Student',
		verbose_name=u"Староста",
		blank=True,
		null=True,
		on_delete=models.SET_NULL)

	notes = models.TextField(
		blank=True,
		verbose_name=u"Додаткові нотатки")

	def __unicode__(self):
		if self.leader:
			return u"{} ({})".format(self.title, self.leader)

		else:
			return u"{}".format(self.title)