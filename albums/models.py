from django.db import models
from artists.models import Artist

class Album(models.Model):
	title = models.CharField(max_length=200)
	cover = models.ImageField(upload_to = 'albums')
	artist = models.ForeignKey(Artist)#Creando la relacion de Artista a albums

	def __unicode__(self):
		return self.title