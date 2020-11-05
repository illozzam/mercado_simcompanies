from django.shortcuts import redirect, resolve_url
from django.views import View

class InitialView(View):
    def get(self, request, **kwargs):
        return redirect(resolve_url('market:buy'))
