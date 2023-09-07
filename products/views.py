from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.
def products(request):
    # Obtener datos del modelo
    products = Product.objects.all()
    
    return render(request, 'products/products.html', {'list_products':products})

def category(request, category_id):
    # category = Category.objects.get(id = category_id)
    product_category = get_object_or_404(Category, id = category_id)
    products = Product.objects.filter(category = product_category)
    
    return render(request, 'products/category.html', {'list_products':products})
