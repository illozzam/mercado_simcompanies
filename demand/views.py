from django.views import View
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import RequestForm
from .models import Request
from market.models import ProductMarket
from django.db.models import Q
from main.models import Log

class RequestListView(LoginRequiredMixin, ListView):
    template_name = 'demand/request_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'demand'
        return context

    def get_queryset(self):
        return Request.objects.filter(done=False).filter(
            Q(user_origin=self.request.user) | Q(user_destination=self.request.user)
        ).order_by('type')

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
            messages.error(self.request, 'Erros no formulário. Verifique e tente novamente.')
            return self.form_invalid(form)
        else:
            messages.success(self.request, 'Requisição cadastrada.')

        return super().form_valid(form)

class RequestMarkDoneView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        product = Request.objects.get(id=kwargs['id_request'])
        if product.user_origin == request.user:
            product.mark_done()

            Log.objects.create(
                user=self.request.user,
                description='{} {} de {} Q{} @ {} - {}.'.format(
                    'Vendeu' if product.type=='V' else 'Comprou',
                    product.quantity,
                    product.product.name,
                    product.quality,
                    product.price,
                    product.user_destination
                )
            )

            messages.success(request, 'Pedido concluído.')
        elif product.user_destination == request.user:
            products_market = ProductMarket.objects.filter(
                owner=product.user_origin,
                type=product.type,
                product=product.product,
                quality=product.quality,
                price=product.price
            )
            if products_market.exists():
                product_on_market = products_market.first()
                product_on_market.quantity += product.quantity
                product_on_market.save()
            else:
                ProductMarket.objects.create(
                    product=product.product,
                    owner=product.user_origin,
                    type=product.type,
                    quantity=product.quantity,
                    quality=product.quality,
                    price=product.price,
                    #description=product.description,
                    #daily_contract=product.daily_contract
                )

            Log.objects.create(
                user=self.request.user,
                description='Cancelou a requisição de {} de {} {} Q{} @ {} - {}.'.format(
                    'compra' if product.type=='V' else 'venda',
                    product.quantity,
                    product.product.name,
                    product.quality,
                    product.price,
                    product.user_origin
                )
            )

            product.delete()
            messages.success(request, 'Pedido cancelado.')
        else:
            messages.error(request, 'Erro ao processar requisição.')
        return redirect('demand:list_request')
