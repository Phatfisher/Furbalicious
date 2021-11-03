from django.contrib import admin
from .models import Furby, Order, CustomUser, OrderFurbies

class FurbyAdmin(admin.ModelAdmin):
    model = Furby

class OrderAdmin(admin.ModelAdmin):
    model = Order

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

class OrderFurbiesAdmin(admin.ModelAdmin):
    model = OrderFurbies

admin.site.register(Furby)
admin.site.register(Order)
admin.site.register(CustomUser)
admin.site.register(OrderFurbies)