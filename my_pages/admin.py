from django.contrib import admin
from .models import Category, Product

# Реєструємо наші моделі, щоб вони з'явилися в адмінці
admin.site.register(Category)
admin.site.register(Product)