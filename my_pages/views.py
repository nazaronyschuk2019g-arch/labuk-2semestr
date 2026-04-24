from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Category, Product, Order
from .forms import RatingForm, NewsletterForm


# --- ЛОГІКА МАГАЗИНУ (Лаби 6-7) ---

def product_list(request, category_id=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    return render(request, 'my_pages/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST' and 'rating_submit' in request.POST:
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            new_rating = rating_form.save(commit=False)
            new_rating.product = product
            new_rating.save()
            return redirect('product_detail', product_id=product.id)
    else:
        rating_form = RatingForm()

    avg_rating = product.ratings.aggregate(Avg('score'))['score__avg']
    if avg_rating:
        avg_rating = round(avg_rating, 1)

    return render(request, 'my_pages/detail.html', {
        'product': product,
        'rating_form': rating_form,
        'avg_rating': avg_rating
    })


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    cart[product_id_str] = cart.get(product_id_str, 0) + 1
    request.session['cart'] = cart
    return redirect('cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_products = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=int(product_id))
        total = product.price * quantity
        total_price += total
        cart_products.append({'product': product, 'quantity': quantity, 'total': total})

    return render(request, 'my_pages/cart.html', {
        'cart_products': cart_products,
        'total_price': total_price
    })


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('product_list')


# --- ЛОГІКА КОРИСТУВАЧІВ (Лаба 8) ---

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    if request.user.is_staff:  # Якщо зайшов адмін
        orders = Order.objects.all().order_by('-created_at')
    else:  # Якщо звичайний юзер
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_pages/profile.html', {'orders': orders})