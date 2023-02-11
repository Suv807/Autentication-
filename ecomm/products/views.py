from pydoc import render_doc
from tkinter import E
from django.shortcuts import render
from products.models import Product, SizeVariant
from django.http import HttpResponseRedirect
from accounts.models import Cart, CartItems


def get_product(request, slug):
    try:  # if anyone type wrong slug we will show 404 page
        product = Product.objects.get(slug=slug)
        return render(request, 'product/product.html', context={'product': product})

    except Exception as e:
        print(e)


def add_to_cart(request, uid):
    variant = request.GET.get('variant')
    product = Product.objects.get(uid=uid)
    user = request.user
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

    cart_items = CartItems.objects.create(cart=cart, product=product)
    if variant:
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size_name=variant)
        cart_items.size_variant = size_variant
        cart_items.save()
    # return HttpResponseRedirect(request.path_info)
