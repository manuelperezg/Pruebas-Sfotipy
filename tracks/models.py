from django.db import models
from albums.models import Album
from artists.models import Artist

#creando el primer modelo (tabla tracks)
class Track(models.Model):
	title = models.CharField(max_length=200)   #un titulo de maximo 200 caracteres
	order = models.PositiveIntegerField() #campo positivo entero
	track_file = models.FileField(upload_to='tracks') #filefield es un campo para subir archivos y se subira a la carpeta de tracks
	album = models.ForeignKey(Album) #relacionando a la tabla album
	artis = models.ForeignKey(Artist) #Relacionando a la tabla artista

	def __unicode__(self):
		return self.title