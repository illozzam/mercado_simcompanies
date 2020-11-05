from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import ProductMarket
from .forms import ProductFilterForm

class BuyView(LoginRequiredMixin, ListView, FormView):
    template_name = 'market/buy.html'
    success_url = reverse_lazy('market:buy')

    def get_form(self):
        return ProductFilterForm()

    def get_queryset(self):
        queryset = ProductMarket.objects.filter(type='V')
        return queryset

class SellView(LoginRequiredMixin, ListView):
    template_name = 'market/sell.html'

    def get_queryset(self):
        queryset = ProductMarket.objects.filter(type='C')
        return queryset
