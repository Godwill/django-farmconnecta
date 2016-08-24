from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from forms import ProductForm
from .models import Product


# Create your views here.
def new_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect('product_details', pk=product.pk)

    else:
        form = ProductForm

    return render(request, 'products/create.html', {'form': form})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product.html', {'product': product})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.published_date = timezone.now()
            product.save()
            return redirect('product_details', pk=product.pk)
        else:
            form = ProductForm(instance=product)

        return render(request, 'products/edit.html', {'form': form})
