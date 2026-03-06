from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def categories_view(req):
    if req.method == 'GET':
        categories = Category.objects.all().order_by('-id')
    return render(req, 'categories.html', {"categories_key": categories})

def products_view(req):
    if req.method == 'GET':
        products = Product.objects.all().order_by('-id')
    return render(req, 'products.html', {"products_key": products})


def category_products_view(req, id):
    if req.method == 'GET':
       
        category = get_object_or_404(Category, id=id)
      
        products = Product.objects.filter(category=category).order_by('-id')
        
    return render(req, 'category_products.html', {
        "category_key": category,
        "products_key": products
    })