from django.shortcuts import render

from .models import Product


def products(request):
    products_list = Product.objects.filter(
        is_active=True
    )

    context = {
        "products": products_list,
    }

    return render(
        request,
        "catalog/products.html",
        context,
    )
