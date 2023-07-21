from django.contrib import admin
from .models import Burger, Pizza

# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')


admin.site.register(Pizza, PizzaAdmin)

class BurgerAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')


admin.site.register(Burger, BurgerAdmin)