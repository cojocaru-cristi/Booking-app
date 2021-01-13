from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')

def evenimente(request: HttpRequest) -> HttpResponse:
    return render(request, 'evenimente.html')

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/profile.html'

def register(response):
    if response.method == "POST":
        form= RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/accounts/login")
    else:
        form = RegisterForm()

    return render(response,'accounts/register.html', {'form': form})
