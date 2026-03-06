from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# 1. Список всех категорий
def categories_view(req):
    if req.method == 'GET':
        categories = Category.objects.all().order_by('-id')
    return render(req, 'categories.html', {"categories_key": categories})

# 2. Все продукты (с сортировкой от новых к старым)
def products_view(req):
    if req.method == 'GET':
        products = Product.objects.all().order_by('-id')
    return render(req, 'products.html', {"products_key": products})

# 3. Продукты конкретной категории
def category_products_view(req, id):
    if req.method == 'GET':
        # Сначала находим саму категорию
        category = get_object_or_404(Category, id=id)
        # Потом фильтруем продукты, которые к ней относятся
        products = Product.objects.filter(category=category).order_by('-id')
        
    return render(req, 'category_products.html', {
        "category_key": category,
        "products_key": products
    })