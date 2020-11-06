from django import forms
from .models import Product

class ProductFilterForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Produto', required=False, widget=forms.Select(attrs={'class': 'form-control mx-2'}))
    quality = forms.ChoiceField(choices=[[x,x] for x in range(0,9)], label='Qualidade', required=False, initial=0, widget=forms.Select(attrs={'class': 'form-control mx-2'}))
    daily_contract = forms.BooleanField(label='Disponível para contrato diário', required=False, initial=False, widget=forms.CheckboxInput(attrs={'class': 'mx-2'}))
