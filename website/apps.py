from django.apps import AppConfig
rom Controllers.Email import email


class WebsiteConfig(AppConfig):
    name = 'website'
    subject = "Test Email"
    message = "This is a test email, please ignore."
    emailList = ["davidgereau@gmail.com"]
    email.sendEmail(subject, message, emailList)