from django.test import TestCase
from django.core import mail
from website.Controllers import Email
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import send_mail

class EmailTestCase(TestCase):

    def test_email(self):
        subject = "Test Email"
        message = "This is a test email, please ignore."
        emailList = ["davidgereau@gmail.com"]
        Email.sendEmail(subject, message, emailList)