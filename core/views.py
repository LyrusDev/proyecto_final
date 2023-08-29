from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def products(request):
    return render(request, 'core/products.html')

def cart(request):
    return render(request, 'core/cart.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')