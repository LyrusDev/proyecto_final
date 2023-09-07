from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Categoría')
    
    # Datos de control
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['created']
    
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    category = models.ForeignKey(Category, verbose_name='Categoría', on_delete=models.PROTECT)
    price = models.FloatField(verbose_name='Precio')
    image = models.ImageField(verbose_name='Imagen', upload_to='products')

    # Datos de control
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['created']

    # Visualizar el título en el gestor de productos
    def __str__(self):
        return self.title
