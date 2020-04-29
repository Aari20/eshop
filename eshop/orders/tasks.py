from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an email notify when an order is successful
    """

    order = Order.objects.get(id=order_id)
    subject = 'Comanda nr. {}'.format(order.id)
    message = 'Draga {}, \n\n Comanda dvs. cu numaru {}' \
              ' a ajuns la noi.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,message, 'aarivps@gmail.com', [order.email])
    return mail_sent
