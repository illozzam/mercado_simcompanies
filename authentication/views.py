from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import UserCreationForm

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'authentication/signup.html'
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        return redirect(self.success_url)
