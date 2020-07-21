from django.contrib import admin

# Register your models here.
from .models import *
from cart.models import Cart


class VarientsAdmin(admin.TabularInline):
    model = Varients
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        VarientsAdmin,
    ]


@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    search_fields = ['title', 'id']


admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Slider)
admin.site.register(Contact)
admin.site.register(Cart)
