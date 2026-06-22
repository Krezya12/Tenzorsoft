from django.urls import path

from apps.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', home, name='home'),
    path('services', home, name='home'),
    path('portfolio', home, name='home'),
    path('contact', home, name='home'),

]