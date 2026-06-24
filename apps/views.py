from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contact_view(request):
    return render(request, 'contact.html')

def portfolio_view(request):
    return render(request, '')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def certificates(request):
    return render(request, 'certificates.html')