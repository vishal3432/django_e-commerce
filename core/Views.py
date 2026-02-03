from django.shortcuts import render, redirect
from .models import Product, Interaction
import numpy as np

# Recommendation Logic (Abhi ke liye Python mein)
def get_recommendations(user):
    products = Product.objects.all()
    if not products.exists():
        return []
    
    # Simple logic: Agar user ne kuch like kiya hai toh usi category ke products dikhao
    liked_categories = Interaction.objects.filter(user=user, score=1).values_list('product__category', flat=True)
    
    if liked_categories:
        recommended = Product.objects.filter(category__in=liked_categories).exclude(
            id__in=Interaction.objects.filter(user=user).values_list('product_id', flat=True)
        )[:4]
        return recommended
    return products.order_by('?')[:4] # Random agar data nahi hai

def product_list(request):
    products = Product.objects.all()
    recommended = []
    
    if request.user.is_authenticated:
        recommended = get_recommendations(request.user)
        
    return render(request, 'shop/home.html', {
        'products': products,
        'recommended': recommended
    })

def like_product(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        Interaction.objects.get_or_create(user=request.user, product=product, score=1)
    return redirect('product_list')