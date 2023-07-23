from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pizza, Burger, Order, Item
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from .forms import NewUserForm
from django.contrib import messages
import random
import json

# Create your views here.
def randomOrderNumber(length):
    sample = 'ABCDEFGH0123456789'
    numberO = ''.join((random.choice(sample) for i in range(length)))
    return numberO


def index(request):
    request.session.set_expiry(0)
    ctx = {'active_link': 'index'}
    return render(request, 'food/index.html', ctx)

@csrf_exempt
def order(request):
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session['note'] = request.POST.get('note')
        request.session['order'] = request.POST.get('orders')
        orders = json.loads(request.session['order'])
        request.session['bill'] = request.POST.get('bill')
        randomNum = randomOrderNumber(6)

        while Order.objects.filter(number=randomNum).count() > 0:
            randomNum = randomOrderNumber(6)
        
        if request.user.is_authenticated:
            order = Order(customer=request.user, 
                            number=randomOrderNumber(6), 
                            bill=float(request.session['bill']),
                            note=request.session['note'])
            order.save()
            request.session['orderNum'] = order.number
            for article in orders:
                item = Item(
                    order = order,
                    name = article[0],
                    price = article[2],
                    size = article[1],
                )
                item.save()

    ctx = {'active_link': 'order'}
    return render(request, 'food/order.html', ctx)

def pizzas(request):
    request.session.set_expiry(0)
    pizzas = Pizza.objects.all()
    ctx = {'pizzas': pizzas, 'active_link': 'pizza'}
    print(pizzas)
    return render(request, 'food/pizza.html', ctx)

def burgers(request):
    request.session.set_expiry(0)
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers, 'active_link': 'burger'}
    print(burgers)
    return render(request, 'food/burger.html', ctx)

def success(request):
    orderNum = request.session['orderNum']
    bill = request.session['bill']
    items = Item.objects.filter(order__number=orderNum)
    ctx = {'orderNum':orderNum, 'bill':bill, 'items':items}
    return render(request, 'food/success.html', ctx)

def signup(request):
    ctx = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            ctx['form'] = form
    else:
        form = NewUserForm()
        ctx['form'] = form
    return render(request, 'food/signup.html', ctx)

def userLogin(request):
    if request.POST:
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username and/or password are incorrect')
    ctx = {'active_link': 'login'}
    return render(request, 'food/login.html', ctx)

def userLogout(request):
    logout(request)
    return redirect('index')