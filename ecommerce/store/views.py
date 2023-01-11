from django.shortcuts import render


def index(request):
    return render(request, 'store/index.html', )


def cart(request):
    return render(request, 'store/cart.html', )


def checkout(request):
    return render(request, 'store/checkout.html', )
