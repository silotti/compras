from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'quantidade']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do item'
            }),
            'quantidade': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            })
        }
