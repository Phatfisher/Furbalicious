from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail

#Sends an email corresponding to the three inputs.
def sendEmail(subject, htmlMessage, recipientList):
    plain_message = strip_tags(htmlMessage)
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, plain_message, email_from, recipientList, html_message=htmlMessage)