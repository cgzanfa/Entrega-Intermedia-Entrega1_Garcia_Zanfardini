from django import forms

class ClienteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    nro_cliente = forms.IntegerField()


class FrutaFormulario(forms.Form):

    fruta = forms.CharField()
    precio = forms.IntegerField()
    nro_articulo = forms.IntegerField()


class VegetalFormulario(forms.Form):

    vegetal = forms.CharField()
    precio = forms.IntegerField()
    nro_articulo = forms.IntegerField()

