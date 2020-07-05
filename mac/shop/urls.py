from django.contrib import admin

from django.urls import path
from . import views

admin.site.site_header = "Login To Vegicle"
admin.site.site_title = "Vegicle"
admin.site.index_title = "Welcome To Vegicle"

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("membership/", views.membership, name="Membership"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("add-to-cart/", views.add_to_cart, name="AddToCart"),
    path("remove-from-cart/", views.remove_from_cart, name="RemoveFromCart"),
    path("cart/", views.get_cart, name="Cart"),
]
