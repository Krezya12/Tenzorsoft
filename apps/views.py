from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.

class HomeListView(ListView):
    template_name = 'home.html'
    