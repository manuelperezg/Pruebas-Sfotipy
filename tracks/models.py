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

#las triples comillas se usan cuando se agregara un script multiline
	#creando un reproductor para el administrador
	def player(self):
		return """      
		<audio controls> 
			<source src = "%s" type="audio/mpeg">
			Tu navegador no soporta este reproductor

		</audio>
		
		"""% self.track_file.url
	player.allow_tags = True #para que trate el codigo o renderize como html
	player.admin_order_field = 'track_file' #para que se pueda ordenar por el reproductor

	def __unicode__(self):
		return self.title