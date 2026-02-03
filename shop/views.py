from django.shortcuts import render, redirect
from .models import Product, Interaction
import numpy as np

def get_recommendations(user):
    # Agar user login nahi hai, toh koi bhi 4 products dikhao
    if not user.is_authenticated:
        return Product.objects.order_by('?')[:4]

    # User ne jo products like kiye hain unki categories nikalna
    liked_categories = Interaction.objects.filter(user=user, score=1).values_list('product__category', flat=True)

    if liked_categories:
        # Same category ke products recommend karna, lekin wo jo abhi tak like nahi kiye
        recommended = Product.objects.filter(category__in=liked_categories).exclude(
            id__in=Interaction.objects.filter(user=user).values_list('product_id', flat=True)
        )[:4]
        
        # Agar recommended kam hain, toh random products add kar dena
        if recommended.count() < 4:
            return Product.objects.order_by('?')[:4]
        return recommended
        
    return Product.objects.order_by('?')[:4]

# --- VIEWS ---

def product_list(request):
    products = Product.objects.all()
    recommended = get_recommendations(request.user)
    
    return render(request, 'shop/home.html', {
        'products': products, 
        'recommended': recommended
    })

def like_product(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        # Interaction record save karna
        Interaction.objects.get_or_create(user=request.user, product=product, score=1)
    
    return redirect('product_list')

def add_to_cart(request, product_id):
    # Session mein cart initialize karna
    cart = request.session.get('cart', {})
    
    # Product ID ko string ki tarah use karna kyunki session JSON use karta hai
    p_id = str(product_id)
    
    if p_id in cart:
        cart[p_id] += 1
    else:
        cart[p_id] = 1
        
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    
    for p_id, quantity in cart.items():
        product = Product.objects.get(id=p_id)
        item_total = product.price * quantity
        total_price += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })
        
    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def checkout(request):
    # Checkout ke baad cart khali kar dena
    request.session['cart'] = {}
    return render(request, 'shop/checkout_success.html')