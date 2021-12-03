from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseRedirect
from django.urls import reverse
from .models import CustomUser, Furby, Order, OrderFurbies
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
        request.user.cardNumber = request.POST['cardNumber']
        request.user.cardExpiry = request.POST['cardExpiry']
        request.user.shippingStreetAddress = request.POST['shippingStreetAddress']
        request.user.shippingState = request.POST['shippingState']
        request.user.shippingZip = request.POST['shippingZip']
        request.user.shippingCountry = request.POST['shippingCountry']

    def post(self, request):
        if request.user.is_authenticated:
            request.user.firstName = request.POST['firstName']
            request.user.lastName = request.POST['lastName'] 
            request.user.email = request.POST['email'] 
            request.user.password = request.POST['password'] 
            request.user.username = request.POST['email']
            request.user.save()
            return redirect('home')

        #Else redirect back to login page
        else:
            return redirect('/login/')

class CartPageView(TemplateView):
    template_name = 'cart.html'

    def get(self, request):

        if 'cart' not in request.session: cart = []
        else: cart = request.session.get('cart')
        print(cart)
        furbies = []
        total = 0

        for furbyId in cart:
            furby = Furby.objects.filter(pk=furbyId).first()
            furbies.append(furby)
            total += furby.cost

        return render(request, 'cart.html', {'furbies': furbies, 'total': total})
            

class OrderHistoryPageView(TemplateView):
    template_name = 'order_history.html'

class HistoryPageView(TemplateView):
    template_name = 'history.html'

class CheckoutPageView(TemplateView):
    template_name = 'checkout.html'

    def post(self, request):
        if request.user.is_authenticated():
            cardNumber = request.POST['cardNumber']
            cardExpiry = request.POST['cardExpiry'] 
            csc = request.POST['CSC'] 
            shippingStreetAddress = request.POST['shippingStreetAddress']
            zip = request.POST['Zip']
            shippingCity = request.POST['shippingCity'] 
            shippingState = request.POST['shippingState']
            shippingCountry = request.POST['shippingCountry']
            
            newOrder = Order(user = request.user, orderDate = datetime.datetime.now(), cardNumber=cardNumber, 
            cardExpiry = cardExpiry, shippingStreetAddress = shippingStreetAddress, shippingCity = shippingCity,
            shippingState = shippingState, shippingCountry = shippingCountry, shippingZip = zip)

            newOrder.save()

            cart = request.session.get('cart')

            for furbyId in cart:
                chosenFurby = Furby.objects.filter(pk=furbyId).first()
                orderFurbies = OrderFurbies(order=newOrder, furby = chosenFurby)
                orderFurbies.save()

            return redirect('home')

        #Else redirect back to login page
        else:
            return redirect('/login/')
    
def logout_request(request):
    logout(request)
    return redirect('home')

#Adds the beloved furby to the cart
def addToCart(request):
    if request.user.is_authenticated:
        furbyID = request.GET.get('furbyID')
        furby = Furby.objects.filter(pk=furbyID).first()

        if furby is not None:
            if 'cart' not in request.session: request.session['cart'] = [furbyID]
            else: 
                request.session['cart'].append(furbyID)
                request.session.save()
            print(furby.furbyName + " added to cart!")
        else: print("I am error.  Furby ID does not exist." + furbyID)
        return redirect('home')

    else:
        print("User not logged in.")
        return redirect('login')

#Removes the selected furby from the cart
def removeFromCart(request):
    if request.user.is_authenticated:
        furbyID = request.GET.get('furbyID')
        furby = Furby.objects.filter(pk=furbyID).first()

        if furby is not None:
            if 'cart' not in request.session: print("Error.  Cart somehow does not exist.  This should not be possible.")
            else: 
                request.session['cart'].remove(furbyID)
                request.session.save()
            print(furby.furbyName + " removed!")

        else: print("I am error.  Furby ID does not exist.")

        return redirect('cart')
    else:
        print("User not logged in.")
        return redirect('login')