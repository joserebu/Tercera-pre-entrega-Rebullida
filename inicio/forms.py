from django import forms

class crear_cocina_formulario(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    tipo_gas = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=500)
    precio = forms.IntegerField()
    
class crear_heladera_formulario(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    tipo_gas = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=500)
    precio = forms.IntegerField()
    
class crear_televisor_formulario(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    tipo_gas = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=500)
    precio = forms.IntegerField()
    
class busqueda_cocina_formulario(forms.Form):
    marca = forms.CharField(max_length=40, required=False)
    
class busqueda_heladera_formulario(forms.Form):
    marca = forms.CharField(max_length=40, required=False)

class busqueda_televisor_formulario(forms.Form):
    marca = forms.CharField(max_length=40, required=False)
    