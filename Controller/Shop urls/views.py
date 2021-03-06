from django.shortcuts import render, get_object_or_404
# Internal Imports
from .models import Category, Product
# Import from cart
from cart.forms import CartAddProductForm


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()  # Cart form
    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def contact(request):
    return render(request, 'shop/product/contact.html')


def about(request):
    return render(request, 'shop/product/about.html')
