from django.shortcuts import redirect, resolve_url
from django.views import View
from django.views.generic import TemplateView
from django.http import Http404
from .models import Page

class InitialView(View):
    def get(self, request, **kwargs):
        return redirect('demand:list_request')

class PageView(TemplateView):
    template_name = 'main/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['page'] = Page.objects.get(url=self.kwargs['url'])
        except:
            raise Http404()
        return context
