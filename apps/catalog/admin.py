
from django.contrib import admin

from .models import (
    Category,
    Collection,
    Product,
    ProductImage,
    ProductLayer,
    ProductSpecification,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification
    extra = 1


class ProductLayerInline(admin.TabularInline):
    model = ProductLayer
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "collection",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "category", "collection")
    search_fields = ("name", "short_description", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_select_related = ("category", "collection")

    inlines = [
        ProductImageInline,
        ProductSpecificationInline,
        ProductLayerInline,
    ]
