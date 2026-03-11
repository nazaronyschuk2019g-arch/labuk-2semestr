from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    # auto_now_add запише час створення, auto_now - час останнього оновлення
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва бренду")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренди"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва товару")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна (грн)")

    # ForeignKey - це те саме об'єднання таблиць, якого вимагає завдання
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return f"{self.name} ({self.brand.name})"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"