from django import forms
from .models import comentarios, publicacion_model

class comentarios_form(forms.ModelForm):
    class Meta:
        model = comentarios
        fields = ('body',)

class nueva_publi_form(forms.ModelForm):

    class Meta:
        model = publicacion_model
        fields = ('title','subtitle','body','imagen')




    