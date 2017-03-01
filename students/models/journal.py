# -*- coding: utf-8 -*-

from django.db import models
from students import Student

class Journal(models.Model):
	"""Journal Model - Модель Журналу Відвідування"""

	class Meta(object):
		verbose_name=u"Група"

	# Продовження тут