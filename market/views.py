from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import ProductMarket
from .forms import ProductFilterForm

class BuyView(LoginRequiredMixin, ListView):
    template_name = 'market/buy.html'

    def get_queryset(self):
        form = ProductFilterForm(self.request.GET)

        filters = {
            'type': 'V',
        }
        if form.is_valid():
            if form.cleaned_data['product']:
                filters['product'] = form.cleaned_data['product']
            if form.cleaned_data['quality']:
                filters['quality__gte'] = form.cleaned_data['quality']
            if form.cleaned_data['daily_contract']:
                filters['daily_contract'] = form.cleaned_data['daily_contract']

        queryset = ProductMarket.objects.filter(**filters).order_by('price')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'buy'
        context['form'] = ProductFilterForm(self.request.GET)
        return context

class SellView(LoginRequiredMixin, ListView):
    template_name = 'market/sell.html'

    def get_queryset(self):
        form = ProductFilterForm(self.request.GET)

        filters = {
            'type': 'C',
        }
        if form.is_valid():
            if form.cleaned_data['product']:
                filters['product'] = form.cleaned_data['product']
            if form.cleaned_data['quality']:
                filters['quality__gte'] = form.cleaned_data['quality']
            if form.cleaned_data['daily_contract']:
                filters['daily_contract'] = form.cleaned_data['daily_contract']

        queryset = ProductMarket.objects.filter(**filters).order_by('price')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'sell'
        context['form'] = ProductFilterForm(self.request.GET)
        return context
