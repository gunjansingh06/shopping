"""
URL configuration for shopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path , include
from customer import views


urlpatterns = [
    path('layout', views.layout, name='layout'),
    path('index', views.index, name='index'),


    path('register', views.register, name='register'),
    path('store_reg', views.store_reg, name='store_reg'),

    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),

    path('contact', views.contact, name='contact'),
    path('store_contact', views.store_contact, name='store_contact'),
    path('delete_contact/<int:id>', views.delete_contact, name='delete_contact'),

    path('product_list/<int:id>/', views.product_list, name='product_list'),
    path('product_detail/<int:id>', views.product_detail, name='product_detail'),

    path('cart', views.cart, name='cart'),
    path('insert_cart', views.insert_cart, name='insert_cart'),
    path('del_cart/<int:id>', views.del_cart, name='del_cart'),

    path('checkout', views.checkout, name='checkout'),
    path('store_checkout', views.store_checkout, name='store_checkout'),

    path('success', views.success, name='success'),
    path('payment', views.payment, name='payment'),

    path('myorders', views.myorders, name='myorders'),
    path('generate_invoice/<int:order_id>/', views.generate_invoice, name='generate_invoice'),

    path('autocomplete/', views.autocomplete, name='autocomplete'),


    


    


    

]


