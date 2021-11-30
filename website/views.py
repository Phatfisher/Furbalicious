from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseRedirect
from django.urls import reverse
from .models import CustomUser, Furby
import uuid
import datetime
from django.utils import timezone


class HomePageView(TemplateView):
    template_name = 'home.html'

# class HomePageListView(ListView):
#     model = Furby

def HomePage(request):
    listing = Furby.objects.all()
    return render(request, 'home.html', {'furbys': listing})


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
            return redirect('home')

        #Else redirect back to login page.  Ideally we need a message system.
        else:
            print('Login Failed for: ' + email + " " + password)
            return redirect('/login/')

class ProfilePageView(TemplateView):
    template_name = 'profile.html'

    def post(self, request):
        if request.user.is_authenticated():
            request.user.firstName = request.POST['firstName']
            request.user.lastName = request.POST['lastName'] 
            request.user.email = request.POST['email'] 
            request.user.password = request.POST['password'] 
            request.user.save()
            return redirect('home')

        #Else redirect back to login page
        else:
            return redirect('/login/')

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

#Adds the beloved furby to the cart
def addToCart(request):
    if request.user.is_authenticated:
        furbyID = request.GET.get('furbyID')
        furby = Furby.objects.filter(pk=furbyID).first()

        if furby is not None:
            if 'cart' not in request.session: request.session['cart'] = [furby]
            else: request.session['cart'].append(furby)
            print(furby.name + " added to cart!")
        else: print("I am error.  Furby ID does not exist." + furbyID)
        return redirect('home')

    else:
        print("User not logged in.")
        return redirect('login')

#Removes the selected furby from the cart
def removeFromCart(request):
    if request.user.is_authenticated():
        furbyID = request.GET['furbyID']
        furby = Furby.objects.get(pk=furbyID)

        if furby is not None:
            if 'cart' not in request.session: print("Error.  Cart somehow does not exist.  This should not be possible.")
            else: request.session['cart'].remove(furby)
        else: print("I am error.  Furby ID does not exist.")

        return redirect('cart')
    else:
        print("User not logged in.")
        return redirect('login')