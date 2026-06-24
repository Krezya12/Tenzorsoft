from django.urls import path
from .views import home, about, services, contact, portfolio, certificates

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),
    path('certificates/', certificates, name='certificates'),
]