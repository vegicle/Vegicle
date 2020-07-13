from django.contrib import admin

# Register your models here.
from .models import *


#
# from shop.models import OrderProduct, Order


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'address', 'city', 'state']


# class OrderProductline(admin.TabularInline):
#     model = OrderProduct
#     readonly_fields = ('user', 'prouct', 'price', 'quantity', 'amount')
#     can_delete = False
#     extra = 0
#
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'username', 'city', 'total', 'status']
#     list_filter = ['filter']
#     readonly_fields = ('user', 'address', 'city', 'state', 'first_name', 'last_name', 'ip', 'total')
#     can_delete = False
#     inlines = [OrderProductline]
#
#
# class OrderProductAdmin(admin.ModelAdmin):
#     list_display = ['user', 'product', 'price', 'quantity', 'amount']
#     list_filter = ['user']


admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderProduct, OrderProduct)
