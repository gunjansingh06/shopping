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
from myadmin import views


urlpatterns = [
    path('layout', views.layout, name='layout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('common_form', views.common_form, name='common_form'),
    path('common_table', views.common_table, name='common_table'),

    path('add_state', views.add_state, name='add_state'),
    path('state_store', views.state_store, name='state_store'),
    path('all_state', views.all_state, name='all_state'),
    path('delete_state/<int:id>', views.delete_state, name='delete_state'),
    path('edit_state/<int:id>', views.edit_state, name='edit_state'),
    path('update_state/<int:id>', views.update_state, name='update_state'),

    path('add_city', views.add_city, name='add_city'),
    path('city_store', views.city_store, name='city_store'),
    path('all_city', views.all_city, name='all_city'),
    path('delete_city/<int:id>', views.delete_city, name='delete_city'),
    path('edit_city/<int:id>', views.edit_city, name='edit_city'),
    path('update_city/<int:id>', views.update_city, name='update_city'),

    path('add_area', views.add_area, name='add_area'),
    path('area_store', views.area_store, name='area_store'),
    path('all_area', views.all_area, name='all_area'),
    path('delete_area/<int:id>', views.delete_area, name='delete_area'),
    path('edit_area/<int:id>', views.edit_area, name='edit_area'),
    path('update_area/<int:id>', views.update_area, name='update_area'),

    path('customer', views.customer, name='customer'),
    path('detail_customer/<int:id>', views.detail_customer, name='detail_customer'),

    path('all_salers', views.all_salers, name='all_salers'),
    path('detail_salers/<int:id>', views.detail_salers, name='detail_salers'),
    
    path('verify/<int:id>', views.verify, name='verify'),
    path('verify1/<int:id>', views.verify1, name='verify1'),


    path('inquiries', views.inquiries, name='inquiries'),

    path('add_categories', views.add_categories, name='add_categories'),
   path('store_categories', views.store_categories, name='store_categories'),
   path('all_categories', views.all_categories, name='all_categories'),
   path('delete_cat/<int:id>', views.delete_cat, name='delete_cat'),
   path('edit_cat/<int:id>', views.edit_cat, name='edit_cat'),
   path('update_cat/<int:id>', views.update_cat, name='update_cat'),

   path('add_subcategories', views.add_subcategories, name='add_subcategories'),
   path('store_subcat', views.store_subcat, name='store_subcat'),
   path('all_subcategories', views.all_subcategories, name='all_subcategories'),
   path('delete_subcat/<int:id>', views.delete_subcat, name='delete_subcat'),
   path('edit_subcat/<int:id>', views.edit_subcat, name='edit_subcat'),
   path('update_subcat/<int:id>', views.update_subcat, name='update_subcat'),

    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),

    path('orders', views.orders, name='orders'),
    path('orders_details/<int:id>', views.orders_details, name='orders_details'),

    path('search_order_orders', views.search_order_orders, name='search_order_orders'),
    
    path('generate_excel_order', views.generate_excel_order, name='generate_excel_order'),
    path('generate_pdf_order', views.generate_pdf_order, name='generate_pdf_order'),


    path('search_order_customer', views.search_order_customer, name='search_order_customer'),
    path('generate_excel_customer', views.generate_excel_customer, name='generate_excel_customer'),
    path('generate_pdf_customer', views.generate_pdf_customer, name='generate_pdf_customer'),
    

    path('search_order_saler', views.search_order_saler, name='search_order_saler'),
    path('generate_excel_saler', views.generate_excel_saler, name='generate_excel_saler'),
    path('generate_pdf_saler', views.generate_pdf_saler, name='generate_pdf_saler'),

    

]


