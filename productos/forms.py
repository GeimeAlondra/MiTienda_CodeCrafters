
from django import forms 
from .models import Producto

class ProductosForm(forms.ModelForm):
    class Meta:
      # date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'})),
      model = Producto
      fields = "__all__"
      widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }
      
   
      
    