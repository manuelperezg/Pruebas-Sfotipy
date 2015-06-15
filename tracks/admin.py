from django.contrib import admin

from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('artis', 'title','order','album','player','es_pharrel') #para agregar campos a mostrar
	list_filter = ('artis','album') #para agregar filtros a buscar
	#search_fields = ('title','artis_first_name','artis_last_name')
	list_editable = ('title','album') #para que los campos se puedan editar desde ahi mismo
	#agilizar la repues(ta para muchos datos en la BD
	raw_id_fields = ('artis',)    #cuando es solo un campo se deja una coma para que no marque error
	#para tener 1000 registros en artis escribimos en la consola
	#./manage.py mockups artis.Artis:1000 y con eso se crearan mil registros

#tratar valores booleanos
	def es_pharrel(self, obj):
		return obj.id ==2
	es_pharrel.boolean = True #poner icono si es o no 


admin.site.register(Track,TrackAdmin)
			