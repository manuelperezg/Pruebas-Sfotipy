import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Track
#creando una vista
def track_view(request, title):
	
	track = get_object_or_404(Track, title = title) #levantando un 404 sino encuentra un track en la url
	data = {
	'title':  track.title,
	'order': track.order,
	'album': track.album.title,
	'artist':{
		'name': track.artis.first_name,
	

		}

	}
	#creando json
	json_data = json.dumps(data)
	return HttpResponse(json_data, content_type = 'application/json')
	#Javascrip Object_Notation (JSON)
	
	#return render(request,'track.html',{'track':track })
	
