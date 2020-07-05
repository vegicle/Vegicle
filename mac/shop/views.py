from django.http import JsonResponse
import sys
sys.path.append('..')
from django.shortcuts import render
from .models import *
from cart.cart import Cart
from decimal import Decimal


# Create your views here.
def varient(args):
    pass


def index(request):
    allProds = []
    slider = Slider.objects.all()
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        allProds.append([prod, range(1, n), n])

    params = {'allProds': allProds, 'slider': slider}
    return render(request, 'shop/index.html', params)


def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)

    return render(request, 'shop/prodView.html', {'product': product[0]})


def checkout(request):
    params = {}
    return render(request, 'shop/checkout.html', params)


def add_to_cart(request, product_id, quantity, price):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    if price in product.varients.all():
        price_num = Decimal(price[:, price.find('r')].replace(',', '.'))
        quantity_num = int(quantity[:, quantity.find('g')])
        cart.add(product, price_num, quantity_num)


def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)


def get_cart(request):
    return render(request, 'shop/cart.html', {'cart': Cart(request)})


def about(request):
    return render(request, 'shop/about.html')


def membership(request):
    return render(request, 'shop/membership.html')


def blog(request):
    return render(request, 'shop/blog.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')
