from __future__ import unicode_literals

from django.db import models

# Create your models here.
class URLMapper(models.Model):
	short_url = models.CharField(max_length=16, unique=True)
	long_url = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "%d-%s-%s" % (self.pk, self.short_url, self.long_url)