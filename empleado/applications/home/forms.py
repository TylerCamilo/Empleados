from django import forms
from .models import Prueba

#creamos una conexion entre el modelo on el formulario para mostrarlo en el html

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""
    class Meta:
        """Meta definition for Pruebaform."""
        model = Prueba
        fields = ('titulo', 'subtitulo', 'cantidad')
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su txt aca widget'
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')       
        if cantidad < 10:
            raise forms.ValidationError('ERROR!!!!!Ingrese un numero mayor a 10')        
        return cantidad
