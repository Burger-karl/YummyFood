from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('pizza', views.pizzas, name='pizzas'),
    path('burger', views.burgers, name='burgers'),

]