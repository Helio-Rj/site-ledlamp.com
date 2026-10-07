from django.urls import path

from .views import (
    about,
    contact,
    content,
    home,
    professionals,
    search,
    technology,
)


urlpatterns = [
    path("", home, name="home"),
    path("sobre/", about, name="about"),
    path("tecnologia/", technology, name="technology"),
    path("profissionais/", professionals, name="professionals"),
    path("conteudo/", content, name="content"),
    path("contato/", contact, name="contact"),
    path("buscar/", search, name="search"),
]
