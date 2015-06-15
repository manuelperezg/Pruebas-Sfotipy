from django.contrib import admin

from .models import Artist
#inlines (permite coontrolar modelos relacionados desde el administrador de un modelo)
#para tener un modificador dentro de otro
from tracks.models import Track
class TrackInline(admin.StackedInline):
	model = Track
	extra = 1

from albums.models import Album
class AlbumInline(admin.StackedInline):
	model = Album
	extra = 1


#creando modelo para buscar un artista entre 1000 registros
class ArtisAdmin(admin.ModelAdmin):
	search_fields = ('first_name','last_name')
	inlines = [AlbumInline, TrackInline]

admin.site.register(Artist, ArtisAdmin)
