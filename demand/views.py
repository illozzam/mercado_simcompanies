from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RequestForm
from .models import Request
from market.models import ProductMarket
from django.db.models import Q

class RequestListView(LoginRequiredMixin, ListView):
    template_name = 'demand/request_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'demand'
        return context

    def get_queryset(self):
        return Request.objects.filter(Q(user_origin=self.request.user) | Q(user_destination=self.request.user)).order_by('type')

class RequestAddView(LoginRequiredMixin, FormView):
    template_name = 'demand/request_new.html'
    success_url = reverse_lazy('demand:list_request')
    form_class = RequestForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_market'] = ProductMarket.objects.get(id=self.kwargs['product_market'])
        context['page'] = 'demand'
        return context

    def form_valid(self, form):
        product = ProductMarket.objects.get(id=self.kwargs['product_market'])
        product_requested = Request().include_product(
            product_market=product,
            user_destination=self.request.user,
            quantity=form.cleaned_data['quantity'],
        )
        if not product_requested:
            form.add_error('quantity', 'Quantidade deve ser menor ou igual a {}'.format(product.quantity))
            return self.form_invalid(form)

        return super().form_valid(form)
