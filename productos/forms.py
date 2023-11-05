
from django import forms 
from .models import Producto
from .models import Contacto





class ProductosForm(forms.ModelForm):
    class Meta:
      # date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'})),
      model = Producto
      fields = "__all__"
      widgets = {
            'fechaVencimiento': forms.DateInput(attrs={'type': 'date'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'})
        }
class ContactoForm(forms.ModelForm):
   class Meta:
    model = Contacto
    fields = "__all__"
     
   
      
    