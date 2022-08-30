from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from django.conf import settings
from django.core.mail import send_mail

# method for updating
@receiver(post_save, sender=User, dispatch_uid="send_mail")
def _send_mail(sender, instance: User, **kwargs):
    if not settings.EMAIL_HOST_USER:
        print("You need to setup `EMAIL_HOST_USER` in settings.py")
        return
    if instance.last_blood_donation_date:
        subject = 'Next blood donation date'
        message = f'Hi {instance.username}, you can donate blood at {instance.get_next_donation_date}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email ]
        send_mail( subject, message, email_from, recipient_list )