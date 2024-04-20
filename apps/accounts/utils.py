import random
import threading

from django.core.mail import EmailMessage
from rest_framework.exceptions import ValidationError


def generate_otp():
    return ''.join(random.choices('0123456789', k=4))


def send_mail_async(email, code):
    try:
        email_msg = EmailMessage(
            'Collegro.uz', f'Your code is - {code}', to=[email])
        email_msg.send()
    except:
        print(code)
        raise ValidationError({
            "success": False,
            "message": "Error has occurred while sending email"
        })


def send_mail(email, code):
    # Create a new thread to send the email asynchronously
    thread = threading.Thread(target=send_mail_async, args=(email, code))
    thread.start()
