from django.shortcuts import render, get_object_or_404, redirect

from .models import Product


def index(request):
    products = Product.objects.all()
    if products:
        return render(request, 'products.html', {'products': products})
    else:
        return redirect('shop:upload')


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_details.html', {'product': product})


def product_buying(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.quantity > 0:
        product.quantity -= 1
        product.save()
        message = 'Your order has been successfully completed'
    else:
        message = "Sorry, we don't have this product in stock"

    return render(request, 'product_buying.html', {'message': message})
