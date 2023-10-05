from django.shortcuts import render, get_object_or_404

from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_details.html', {'product': product})


