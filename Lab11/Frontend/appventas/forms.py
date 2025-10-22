from django import forms


class FileForm(forms.Form):
    #Es necesario identificar el archivo del label
    file = forms.FileField(label='file') #campos tipo archivo (hay diferentes tipos) Ej: forms.ChoiceField (son los selects), forms.URLField

    
class InputTextAreaForm(forms.Form):
    entrada = forms.CharField(label='entrada')