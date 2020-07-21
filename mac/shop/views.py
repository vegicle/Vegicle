from django.http import JsonResponse
import sys

sys.path.append('..')
from django.shortcuts import render
from .models import *
from cart.cart import Cart
from cart.models import Item
from decimal import Decimal
from user.models import UserProfile


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
    instruction = Instruction.objects.get(title='checkout-instruction')
    subtotal = 0
    items_count = 0
    cart = list()

    user = None
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)

    for item in Cart(request):
        subtotal = item.total_price + subtotal
        items_count = items_count + 1
        varient = Varients.objects.get(id=item.product_varient_id)
        cart.append({'item': item, 'varient': varient})

    if request.method == 'GET':
        if subtotal < instruction.min_coast:
            return render(request, 'shop/checkout.html', {'instruction': instruction.instruction_message,
                                                          'cart': cart, 'subtotal': subtotal,
                                                          'items_count': items_count, 'user': user})
        else:
            return render(request, 'shop/checkout.html', {'cart': cart, 'subtotal': subtotal,
                                                          'items_count': items_count, 'user': user})
    if request.method == 'POST':
        if subtotal >= instruction.min_coast:
            print(request.POST)

            firstName = request.POST.get('firstName', '')
            lastName = request.POST.get('lastName', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('username', '')
            address = request.POST.get('address', '')
            city = request.POST.get('city', '')
            Order.objects.create(firstName=firstName, lastName=lastName, email=email, phone=phone, address=address,
                                 city=city)

            return JsonResponse({"status": "The order was created successfully", "code": 0})
        else:
            return JsonResponse({"status": instruction.instruction_message, "code": 1})
        pass


def add_to_cart(request):
    product_id = request.POST.get('product_id')
    price = Decimal(request.POST.get('price'))

    product = Product.objects.get(id=product_id)
    product_varient = product.varients.all().get(price=price)
    cart = Cart(request)
    cart.add(product, product_varient.price, product_varient.id)
    return JsonResponse({'message': 'successful'}, status=200)


def remove_from_cart(request):
    product_id = int(request.POST.get('product_id'))
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return JsonResponse({'message': 'successful'}, status=200)


def update_cart_item(request):
    item_id = int(request.POST.get('item_id'))
    new_quantity = int(request.POST.get('new_quantity'))
    item_to_update = Item.objects.get(id=item_id)
    item_to_update.quantity = new_quantity
    item_to_update.save()
    return JsonResponse({'message': 'successful'}, status=200)


def get_cart(request):
    subtotal = 0
    cart = list()
    for item in Cart(request):
        subtotal = item.total_price + subtotal
        varient = Varients.objects.get(id=item.product_varient_id)
        cart.append({'item': item, 'varient': varient})
    return render(request, 'shop/cart.html', {'cart': cart, 'subtotal': subtotal})


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


# def orderproduct(request):
#     current_user = request.user
#     shopcart = ShopCart.objects.filter

