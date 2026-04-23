from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# Сторінка всіх товарів або певної категорії
def product_list(request, category_id=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    # Якщо передано ID категорії, фільтруємо товари
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    return render(request, 'my_pages/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


# Сторінка одного товару
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'my_pages/detail.html', {'product': product})