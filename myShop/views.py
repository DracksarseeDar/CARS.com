from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Category, Product


class CategoryListView(generic.ListView):
    template_name = 'categories.html'
    model = Category
    context_object_name = 'categories_key'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class ProductListView(generic.ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products_key'

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')


class CategoryProductDetailView(generic.ListView):
    template_name = 'category_products.html'
    model = Product
    context_object_name = 'products_key'

    def get_queryset(self):
        category_id = self.kwargs.get('id')
        return self.model.objects.filter(category__id=category_id).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_key'] = get_object_or_404(Category, id=self.kwargs.get('id'))
        return context

# def categories_view(req):
#     if req.method == 'GET':
#         categories = Category.objects.all().order_by('-id')
#     return render(req, 'categories.html', {"categories_key": categories})

# def products_view(req):
#     if req.method == 'GET':
#         products = Product.objects.all().order_by('-id')
#     return render(req, 'products.html', {"products_key": products})


# def category_products_view(req, id):
#     if req.method == 'GET':
       
#         category = get_object_or_404(Category, id=id)
      
#         products = Product.objects.filter(category=category).order_by('-id')
        
#     return render(req, 'category_products.html', {
#         "category_key": category,
#         "products_key": products
#     })