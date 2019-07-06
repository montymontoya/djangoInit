from django import forms
from django.forms import ModelForm
from .models import impresiones3d

class loginForm(forms.Form):
    usuario = forms.CharField(label = 'Usuario', max_length = 40 )
    password = forms.CharField(label = 'Contraseña', max_length = 40)

class registerForm(forms.Form):
    nombre = forms.CharField(label = 'Nombre', max_length = 40 )
    usuario = forms.CharField(label = 'Usuario', max_length = 40 )
    correo = forms.CharField(label = 'e-mail', max_length = 40 )
    password = forms.CharField(label = 'Contraseña', max_length = 40)
    nacimiento = forms.DateField(label = 'Nacimientio', widget=forms.SelectDateWidget)
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices = [('h','Hombre'),('m','Mujer')])

class registrarImpresion(ModelForm):
    class Meta:
        model = impresiones3d
        fields = ['nombre','gramaje', 'tiempo', 'cantidad', 'filamento', 'picture']

    