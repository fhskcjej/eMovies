from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Cart
from purchases.models import Purchase
from users.models import Card
from django.contrib.auth.decorators import login_required
from eMovies_app.models import Movie


def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.error(request, "Ваша корзина пуста.")
        return redirect('view_cart')

    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiration_date = request.POST.get('expiration_date')
        cvv = request.POST.get('cvv')

        if not all([card_number, expiration_date, cvv]):
            messages.error(request, "Пожалуйста, заполните все поля.")
            return redirect('checkout')

        # Сохраняем или обновляем карту
        Card.objects.update_or_create(
            user=request.user,
            defaults={
                'card_number': card_number,
                'expiration_date': expiration_date,
                'CVV': cvv
            }
        )

        # Оформляем покупку: создаём записи в Purchase
        for item in cart_items:
            Purchase.objects.get_or_create(
                user=request.user,
                movie=item.movie
            )

        # Очищаем корзину
        cart_items.delete()

        messages.success(request, "Покупка успешно завершена!")
        return redirect('purchase_complete')

    return render(request, 'cart/checkout.html', {
        'cart_items': cart_items,
        'total_price': sum(item.movie.price for item in cart_items)
    })


@login_required
def add_to_cart(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, movie=movie)
    if created:
        message = f"Фильм «{movie.title}» добавлен в корзину."
    else:
        message = f"Фильм «{movie.title}» уже в корзине."
    return redirect("cart:cart")


@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.movie.price for item in cart_items if item.movie.price)
    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total_price": total_price
    })


@login_required
def remove_from_cart(request, movie_id):
    cart_item = Cart.objects.filter(user=request.user, movie_id=movie_id).first()
    if cart_item:
        cart_item.delete()
    return redirect("cart:cart")


@login_required
def clear_cart(request):
    Cart.objects.filter(user=request.user).delete()
    return redirect("cart:cart")

