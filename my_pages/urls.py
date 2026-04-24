from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # --- Маршрути магазину (Лаби 6-7) ---
    path('', views.product_list, name='product_list'),
    path('category/<int:category_id>/', views.product_list, name='category_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('subscribe/', views.subscribe, name='subscribe'),

    # --- Маршрути користувачів (Лаба 8) ---
    path('accounts/', include('django.contrib.auth.urls')), # Вбудовані шляхи для логіну/виходу
    path('register/', views.register, name='register'), # Реєстрація
    path('profile/', views.profile, name='profile'), # Особистий кабінет
]