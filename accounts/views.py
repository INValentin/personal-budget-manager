from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.


class AccountLoginView(LoginView):
    success_url = reverse_lazy("budgets:home")
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

class AccountCreateView(FormView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/create.html"
    redirect_authenticated_user = True
    
    
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('home'))
        
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('home'))
        
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        if form.is_valid():
            form.save()
        
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")
    
    def get(self, request, *args, **kwargs):
        return  HttpResponseNotAllowed(['POST'])
    