import re
from django.http import HttpResponse
from django.shortcuts import render

import products
from .models import Product

# Create your views here.
# /products -> index
# Uniform Resource Locator (Address)
def index(request):
    products = Product.objects.all()
    # Product.objects.filter()
    # Product.objects.save()
    # return HttpResponse('Hello World')
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')

