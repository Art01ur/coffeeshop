from django.shortcuts import redirect

from shop.models import Type, Product
from .data_for_db import product_type_list, product_list


def create_one_type(product_type):
    type = Type(title=product_type['title'])
    type.save()


def create_one_product(product_data):
    product = Product(
        name=product_data['name'],
        price=product_data['price'],
        country=product_data['country'],
        roast=product_data['roast'],
        type=Type.objects.get(pk=product_data['type_id']),
        quantity=product_data['quantity']
    )

    product.save()


def upload_data(request):
    for pr_type in product_type_list:
        create_one_type(pr_type)

    for pr in product_list:
        create_one_product(pr)

    return redirect('shop:index')
