from django.shortcuts import render


def home(request):
    context = {
        "page": "Home",
    }

    return render(
        request,
        "index.html",
        context
    )


def all_cities(request):
    context = {
        "page": "Available Cities",
    }

    return render(
        request,
        "all_cities.html",
        context
    )
