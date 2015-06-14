from django.db import models

class Artist(models.Model):
	first_name = models.CharField(max_length=200) #charFiel es un input
	last_name = models.CharField(max_length=200,blank=True) 
	biography = models.TextField(blank=True) #textFiel es un campo de texto

	def __unicode__(self):
		return self.first_name
