from django.shortcuts import render
# Імпортуємо наші таблиці з бази даних
from .models import Category, Product


def home_view(request):
    # Дістаємо ВСІ категорії та ВСІ товари з бази
    categories = Category.objects.all()
    products = Product.objects.all()

    context = {
        'title': 'Cloud City - Головна',
        'categories': categories,  # Передаємо категорії для меню
        'products': products,  # Передаємо товари для вітрини
        'is_main': True
    }
    return render(request, 'my_pages/base.html', context)


def page1_view(request):
    categories = Category.objects.all()
    context = {
        'title': 'Про нас',
        'categories': categories,
        'is_main': False
    }
    return render(request, 'my_pages/base.html', context)


def page2_view(request):
    categories = Category.objects.all()
    context = {
        'title': 'Контакти',
        'categories': categories,
        'is_main': False
    }
    return render(request, 'my_pages/base.html', context)