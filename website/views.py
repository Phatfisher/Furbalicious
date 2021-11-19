from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseRedirect
from django.urls import reverse
from .models import CustomUser, Furby
import uuid
import datetime

class HomePageView(TemplateView):
    template_name = 'home.html'

class RegistrationPageView(TemplateView):
    template_name = 'registration.html'

    #Handles registration attempt
    def post(self, request):
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        emailAddress = request.POST['email']
        password = request.POST['password']
        confirmationCode = uuid.uuid4().hex

        #Check if email is already in use, if not create user
        user = CustomUser.objects.filter(email=emailAddress).first()
        if user is None:
            newUser = CustomUser.objects.create_user(firstName = firstName, lastName = lastName, email=emailAddress, 
            confirmation = confirmationCode, username = emailAddress, password = password)

            newUser.save()
            login(request, newUser)
            print(' SuccLoginessful')
            return HttpResponseRedirect(reverse('home'))

        else:
            print('Registration Failed:  Email in use')
            return redirect('/registration/')

class LoginPageView(TemplateView):
    template_name = 'login.html'

    #Handles login attempt
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        #If user found in DB, login user and send to catalog.
        if user is not None:
            login(request, user)
            print('Login Successful')
            return HttpResponseRedirect(reverse('home'))
        #Else redirect back to login page.  Ideally we need a message system.
        else:
            print('Login Failed for: ' + email + " " + password)
            return redirect('/login/')

class ProfilePageView(TemplateView):
    template_name = 'profile.html'

class CartPageView(TemplateView):
    template_name = 'cart.html'

class OrderHistoryPageView(TemplateView):
    template_name = 'order_history.html'

class HistoryPageView(TemplateView):
    template_name = 'history.html'

class CheckoutPageView(TemplateView):
    template_name = 'checkout.html'
    
def logout_request(request):
    logout(request)
    return redirect('home')