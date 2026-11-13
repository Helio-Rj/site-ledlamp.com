from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="nome",
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        verbose_name="slug",
    )

    description = models.TextField(
        blank=True,
        verbose_name="descrição",
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
