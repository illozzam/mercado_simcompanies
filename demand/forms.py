from django import forms

class RequestForm(forms.Form):
    quantity = forms.IntegerField(label='Quantidade desejada', required=True, min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
