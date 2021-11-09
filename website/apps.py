from django.apps import AppConfig
from Controllers import Email


class WebsiteConfig(AppConfig):
    name = 'website'
    subject = "Test Email"
    message = "This is a test email, please ignore."
    emailList = ["davidgereau@gmail.com"]
    Email.sendEmail(subject, message, emailList)