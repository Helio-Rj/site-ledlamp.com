
from django.db.models import Prefetch
from django.shortcuts import render

from .models import Product, ProductImage


def products(request):
    product_images = ProductImage.objects.order_by(
        "-is_primary",
        "position",
        "id",
    )

    products_list = (
        Product.objects
        .filter(is_active=True)
        .prefetch_related(
            Prefetch(
                "images",
                queryset=product_images,
            )
        )
    )

    context = {
        "products": products_list,
    }

    return render(
        request,
        "catalog/products.html",
        context,
    )
