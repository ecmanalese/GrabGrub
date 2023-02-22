"""GrabGrub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('view_orders', views.view_orders, name='view_orders'),
    path('view_order_details/<int:pk>/', views.view_order_details, name='view_order_details'),
    path('update_order/<int:pk>/', views.update_order, name='update_order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),
    path('view_food' , views.view_food, name='view_food'),
    path('view_food_details/<int:pk>/', views.view_food_details, name='view_food_details'),
    path('update_food/<int:pk>/', views.update_food, name='update_food'),
    path('delete_food/<int:pk>/', views.delete_food, name='delete_food'),
    path('add_food', views.add_food, name='add_food'),
    path('view_customer', views.view_customer, name='view_customer'),
    path('view_customer_details/<int:pk>/', views.view_customer_details, name='view_customer_details'),
    path('update_customer/<int:pk>/', views.update_customer, name='update_customer'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),
]
