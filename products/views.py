import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
# /products -> index
# Uniform Resource Locator (Address)
def index(request):
    Product.objects.all()
    # Product.objects.filter()
    # Product.objects.save()
    # return HttpResponse('Hello World')
    return render(request, 'index.html')


def new(request):
    return HttpResponse('New Products')

