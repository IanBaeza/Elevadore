from django import forms

from .models import Cliente, Orden
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields = [
			'nombre',
			'direccion',
			'ciudad',
			'comuna',
			'email',
			'telefono',
		]
		labels = {
			'nombre': 'Nombre',
			'direccion': 'Direccion',
			'ciudad': 'Ciudad',
			'comuna': 'Comuna',
			'email': 'Email',
			'telefono': 'Telefono',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'ciudad': forms.TextInput(attrs={'class':'form-control'}),
			'comuna': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control','type':'email'}),
			'telefono': forms.TextInput(attrs={'class':'form-control','type':'number'}),

		}
		
class OrdenForm(forms.ModelForm):
	class Meta:

		model = Orden
		fields =[
			'cliente',
			'fecha',
			'horainicio',
			'horafin',
			'idascensor',
			'modeloasc',
			'fallas',
			'reparaciones',
			'piezascambiadas',
			'receptor',
			'tecnico',
		]
		labels = {
			'cliente': 'Cliente Asociado',
			'fecha': 'Fecha de Trabajo',
			'horainicio': 'Hora de Inicio',
			'horafin': 'Hora de Fin',
			'idascensor': 'Código de Ascensor',
			'modeloasc': 'Modelo ',
			'fallas': 'Fallas detectadas',
			'reparaciones': 'Reparaciones realizadas',
			'piezascambiadas': 'Piezas reemplazadas',
			'receptor': 'Receptor de trabajo',
			'tecnico': 'Tecnico encargado',
		}
		widgets = {
			'cliente': forms.Select(attrs={'class': 'form-control col-12 justify-content-center'	}),
			'fecha': forms.SelectDateWidget(attrs={'class':'form-control col-12 justify-content-center'}),
			'horainicio': forms.TextInput(attrs={'class':'form-control col-12 justify-content-center','type':'time'}),
			'horafin': forms.TextInput(attrs={'class':'form-control col-12 justify-content-center' ,'type':'time'}),
			'idascensor': forms.TextInput(attrs={'class':'form-control col-12 justify-content-center','type':'number'}),
			'modeloasc': forms.TextInput(attrs={'class':'form-control col-12 justify-content-center'}),
			'fallas': forms.TextInput(attrs={'class':'form-control col-12 justify-content-center' }),
			'reparaciones': forms.TextInput(attrs={'class':'form-control col-12 justify-content-center'}),
			'piezascambiadas': forms.TextInput(attrs={'class':'form-control col-12 justify-content-center'}),
			'receptor': forms.TextInput(attrs={'class':'form-control col-12 justify-content-center'}),
			'tecnico': forms.Select(attrs={'class': 'form-control col-12 justify-content-center'}),
		}

class RegistroForm(UserCreationForm):

	class Meta:
		model = User

		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		help_texts={
				'username': None,
		}
		labels = {
				'username': 'Nombre de Usuario',
				'first_name': 'Nombres',
				'last_name': 'Apellidos',
				'email': 'Correo Electronico',
		}
