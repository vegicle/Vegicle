from xml.etree.ElementInclude import include

from django.contrib import admin

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("update/", views.user_update, name="user_update"),
    path("password/", views.user_password, name="user_password"),
    # path("orders/", views.user_orders, name="user_orders"),
]

