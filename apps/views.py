from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contact_view(request):
    return render(request, '')

def portfolio_view(request):
    return render(request, '')

