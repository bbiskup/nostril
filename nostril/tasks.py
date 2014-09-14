from __future__ import absolute_import
from celery import shared_task
from celery.exceptions import Ignore
from django.core.mail import send_mail as dj_send_mail


@shared_task
def mul(x, y):
    return x * y


@shared_task(ignore_result=True)
def dummy_output(message):
    print('Message: {0}'.format(message))


@shared_task(ignore_result=True)
def dummy_output_ignore_state(message):
    print('Message: {0}'.format(message))
    raise Ignore()


@shared_task
def pow(x, y):
    return x ** y


@shared_task
def send_mail(subject, message, from_email, recipient_list):
    dj_send_mail(subject,
                message,
                from_email,
                recipient_list)