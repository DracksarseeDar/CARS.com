from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50 , verbose_name="Введите Категорию")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.PositiveIntegerField(verbose_name="Цена")
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        # Здесь мы выводим название товара и его категорию
        return f"{self.name} - {self.price} - {self.category.name}"