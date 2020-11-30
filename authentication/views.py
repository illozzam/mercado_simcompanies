from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from main.models import Log
from .forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'authentication/signup.html'
    success_url = '/login/'

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Usuário cadastrado com sucesso. Faça login para continuar.')
        Log.objects.create(
            user=user,
            description='Cadastro de usuário.'
        )
        return redirect(self.success_url)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserChangeForm
    template_name = 'authentication/user_update.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Dados atualizados.')
        Log.objects.create(
            user=user,
            description='Usuário editou seus dados.'
        )
        return redirect(self.success_url)

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'authentication/password_change.html'
    success_url = '/'

    def form_valid(self, form):
        Log.objects.create(
            user=self.request.user,
            description='Alterou a senha.'
        )
        messages.success(self.request, 'Senha alterada com sucesso.')
        return super().form_valid(form)
