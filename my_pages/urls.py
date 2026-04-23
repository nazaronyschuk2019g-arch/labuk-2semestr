from django.urls import path
from . import views

urlpatterns = [
    # Всі товари
    path('', views.product_list, name='product_list'),
    # Товари по категоріях
    path('category/<int:category_id>/', views.product_list, name='category_list'),
    # Конкретний товар
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]