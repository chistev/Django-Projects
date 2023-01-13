from django.shortcuts import render
from .models import *


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/index.html', context )


def cart(request):
    return render(request, 'store/cart.html', )


def checkout(request):
    return render(request, 'store/checkout.html', )
