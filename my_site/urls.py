from django.contrib import admin
from django.urls import path, include  # <--- Додали слово include через кому

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_pages.urls')), # <--- Додали цей рядок, щоб підключити твою аплікуху
]