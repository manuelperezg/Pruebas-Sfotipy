from django.shortcuts import render
from django.contrib.auth import login

from .forms import UserCreationEmailForm, EmailAuthenticationForm
# creando el formulario de inicio de sesion.
def signup(request):
	form= UserCreationEmailForm(request.POST or None) #crear el formulario si hay datos post entonces llene los datos sino hay nada que se cree vacio
	
	if form.is_valid():
		form.save()
	#retornando un html
	return render(request, 'signup.html',{'form':form})

#no llamar a la vista login por que es una funcion reservada
#creando vista entrar
def signin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		
		login(request, form.get_user())

	return render(request, 'signin.html', {'form': form})