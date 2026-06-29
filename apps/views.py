import re

from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .models import ContactMessage


PHONE_RE = re.compile(r'^\+?[0-9\s\-\(\)]{7,20}$')

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not phone or not message:
            messages.error(request, _('Iltimos, majburiy maydonlarni to‘ldiring.'))
        elif not PHONE_RE.fullmatch(phone):
            messages.error(request, _('Telefon raqamiga faqat raqam kiriting.'))
        else:
            ContactMessage.objects.create(
                name=name,
                phone=phone,
                email=email,
                message=message,
            )
            messages.success(request, _('Xabaringiz qabul qilindi. Tez orada siz bilan bog‘lanamiz.'))
            return redirect('contact')

    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def certificates(request):
    return render(request, 'certificates.html')
