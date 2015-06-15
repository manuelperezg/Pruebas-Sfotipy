from django import forms 
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#heredando el formulario de django original para crear usuarios

class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ('username','email')

class EmailAuthenticationForm(forms.Form):
	email = forms.EmailField()
	password = forms.CharField(label = 'Password', widget=forms.PasswordInput)
	#creando un contructor
	def __init__(self, *args, **kwargs):
		self.user_cache = None #el usuario que voy a validad este vacio
		super(EmailAuthenticationForm, self).__init__(*args, **kwargs)

		#validar que el usuario exista que haya un usuario con ese email y ese password
	def clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')

		self.user_cache = authenticate(email = email, password = password)

		if self.user_cache is None:
			raise form.ValidationError('Usuario incorrecto')
		elif not self.user_cache.is_active:
			raise form.ValidationError('Usuario inactivo')

		return self.cleaned_data
		#si todo paso bien el usuario se guardo en la cache

		def get_user(self):
			return self.user_cache 

