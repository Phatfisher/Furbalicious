from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class RegistrationPageView(TemplateView):
    template_name = 'registration.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class ProfilePageView(TemplateView):
    template_name = 'profile.html'

class CartPageView(TemplateView):
    template_name = 'cart.html'

class OrderHistoryPageView(TemplateView):
    template_name = 'order_history.html'

class CheckoutPageView(TemplateView):
    template_name = 'checkout.html'
