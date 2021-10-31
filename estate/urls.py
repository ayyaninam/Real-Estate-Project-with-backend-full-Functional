from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('all-properties', views.all_properties),
    path('property/<int:sno>', views.single_property_page),
    path('login', views.login),
    path('signup', views.signup),
    path('logout', views.logout),
    path('dealer-register', views.dealer_register),
    path('dealer-dashboard', views.dealer_dashboard),
    path('create-property', views.create_property),
    path('delete-property/<int:sno>', views.delete_property),
    path('edit-property/<int:sno>', views.edit_property),
    path('search', views.search),
    path('buy', views.buy),
    path('sell', views.sell),
    path('rent', views.rent),
]
