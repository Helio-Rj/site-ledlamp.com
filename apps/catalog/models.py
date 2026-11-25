
from django.db import models
from django.db.models import Q


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="nome",
    )
    slug = models.SlugField(
        max_length=170,
        unique=True,
        verbose_name="slug",
    )
    description = models.TextField(
        blank=True,
        verbose_name="descrição",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="ativa",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="nome",
    )
    slug = models.SlugField(
        max_length=170,
        unique=True,
        verbose_name="slug",
    )
    description = models.TextField(
        blank=True,
        verbose_name="descrição",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="ativa",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "coleção"
        verbose_name_plural = "coleções"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products",
        null=True,
        blank=True,
        verbose_name="categoria",
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="coleção",
    )
    name = models.CharField(
        max_length=200,
        verbose_name="nome",
    )
    slug = models.SlugField(
        max_length=220,
        unique=True,
        verbose_name="slug",
    )
    short_description = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="descrição curta",
    )
    description = models.TextField(
        blank=True,
        verbose_name="descrição completa",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="ativo",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="criado em",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="atualizado em",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "produto"
        verbose_name_plural = "produtos"

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="specifications",
        verbose_name="produto",
    )
    name = models.CharField(
        max_length=150,
        verbose_name="característica",
    )
    value = models.CharField(
        max_length=250,
        verbose_name="valor",
    )
    unit = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="unidade",
    )
    position = models.PositiveIntegerField(
        default=0,
        verbose_name="ordem de exibição",
    )

    class Meta:
        ordering = ["position", "name"]
        verbose_name = "especificação técnica"
        verbose_name_plural = "especificações técnicas"

    def __str__(self):
        return f"{self.name}: {self.value}"


class ProductLayer(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="layers",
        verbose_name="produto",
    )
    name = models.CharField(
        max_length=150,
        verbose_name="nome da camada",
    )
    material = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="material",
    )
    description = models.TextField(
        blank=True,
        verbose_name="descrição",
    )
    function = models.TextField(
        blank=True,
        verbose_name="função da camada",
    )
    position = models.PositiveIntegerField(
        default=0,
        verbose_name="ordem de exibição",
    )

    class Meta:
        ordering = ["position"]
        verbose_name = "camada do produto"
        verbose_name_plural = "camadas dos produtos"

    def __str__(self):
        return f"{self.product.name} - {self.name}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="produto",
    )
    image = models.ImageField(
        upload_to="catalog/products/",
        verbose_name="arquivo da imagem",
    )
    alt_text = models.CharField(
        max_length=200,
        verbose_name="texto alternativo",
    )
    caption = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="legenda",
    )
    is_primary = models.BooleanField(
        default=False,
        verbose_name="imagem principal",
    )
    position = models.PositiveIntegerField(
        default=0,
        verbose_name="ordem de exibição",
    )

    class Meta:
        ordering = ["position", "id"]
        verbose_name = "imagem do produto"
        verbose_name_plural = "imagens dos produtos"
        constraints = [
            models.UniqueConstraint(
                fields=["product"],
                condition=Q(is_primary=True),
                name="unique_primary_image_per_product",
            ),
        ]

    def __str__(self):
        return f"Imagem de {self.product.name}"
