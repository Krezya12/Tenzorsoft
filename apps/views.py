import logging
import os
import re
import threading
import requests

from dotenv import load_dotenv
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _

from .models import ContactMessage

PHONE_RE = re.compile(r'^\+?[0-9\s\-\(\)]{7,20}$')

load_dotenv()


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

            threading.Thread(
                target=send_telegram_notification,
                args=(name, phone, email, message),
                daemon=True  # daemon=True означает, что поток не заблокирует остановку сервера
            ).start()

            messages.success(request, _('Xabaringiz qabul qilindi. Tez orada siz bilan bog‘lanamiz.'))
            return redirect('contact')

    return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def certificates(request):
    return render(request, 'certificates.html')


logger = logging.getLogger(__name__)

def send_telegram_notification(name, phone, email, message):
    """Функция, которая будет выполняться в отдельном потоке"""
    # Получаем данные напрямую из переменных окружения
    bot_token = os.environ.get('BOT_TOKEN')
    chat_id = os.environ.get('ADMIN_CHAT_ID')

    if not bot_token or not chat_id:
        logger.error("Telegram BOT_TOKEN or ADMIN_CHAT_ID is not configured in environment variables.")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    text = (
        f"🔔 **Yangi xabar!**\n\n"
        f"👤 **Ism:** {name}\n"
        f"📞 **Telefon:** {phone}\n"
        f"📧 **Email:** {email or 'Ko‘rsatilmagan'}\n"
        f"💬 **Xabar:** {message}"
    )

    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Telegram yuborishda xatolik: {e}")
