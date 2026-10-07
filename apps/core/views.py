from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def technology(request):
    return render(request, "core/technology.html")


def professionals(request):
    return render(request, "core/professionals.html")


def content(request):
    return render(request, "core/content.html")


def contact(request):
    return render(request, "core/contact.html")


def search(request):
    return render(request, "core/search.html")
