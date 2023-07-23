from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('pizza', views.pizzas, name='pizzas'),
    path('burger', views.burgers, name='burgers'),
    path('order', views.order, name='order'),
    path('success', views.success, name='success'),
    path('signup', views.signup, name='signup'),
    path('login', views.userLogin, name='login'),
    path('logout', views.userLogout, name='logout'),

]