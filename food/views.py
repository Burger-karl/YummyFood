from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza, Burger

# Create your views here.
def index(request):
    ctx = {'active_link': 'index'}
    return render(request, 'food/index.html', ctx)

def order(request):
    ctx = {'active_link': 'order'}
    return render(request, 'food/order.html', ctx)

def pizzas(request):
    pizzas = Pizza.objects.all()
    ctx = {'pizzas': pizzas, 'active_link': 'pizza'}
    print(pizzas)
    return render(request, 'food/pizza.html', ctx)

def burgers(request):
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers, 'active_link': 'burger'}
    print(burgers)
    return render(request, 'food/burger.html', ctx)
