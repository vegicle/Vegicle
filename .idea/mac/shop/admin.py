from django.contrib import admin

# Register your models here.
from .models import *
from cart.models import Cart


class VarientsAdmin(admin.TabularInline):
    model = Varients
    min_num = 1
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        VarientsAdmin,
    ]


admin.site.register(Customer)
admin.site.register(Slider)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
admin.site.register(Cart)
