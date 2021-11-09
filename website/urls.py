from django.urls import path
import website.views as views

urlpatterns = [
    path('', views.HomePageView.as_view(), name ='home'),
    path('registration/', views.RegistrationPageView.as_view(), name='registration'),
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('profile/', views.ProfilePageView.as_view(), name='profile'),
    path('cart/', views.CartPageView.as_view(), name='cart'),
    path('checkout/', views.CheckoutPageView.as_view(), name='checkout'),
]