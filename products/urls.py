from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('category/<int:category_id>/', views.category, name='category')
]