from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from forms import VendorProductForm
from .models import VendorProduct


# Create your views here.
def vendor_product_list(request):
    vendor_products = VendorProduct.objects.filter().order_by('published_date')
    return render(request, 'vendor_products/index.html', {'vendor_products': vendor_products})


def new_vendor_product(request):

    if request.method == 'POST':
        form = VendorProductForm(request.POST, request.FILES)
        if form.is_valid():
            vendor_product = form.save(commit=False)
            vendor_product.user = request.user
            vendor_product.published_date = timezone.now()
            vendor_product.save()
            return redirect('product_details', pk=vendor_product.pk)

    else:
        form = VendorProductForm

    return render(request, 'vendor_products/create.html', {'form': form})


def vendor_product_details(request, pk):
    vendor_product = get_object_or_404(VendorProduct, pk=pk)
    return render(request, 'vendor_products/product.html', {'vendor_product': vendor_product})


def edit_vendor_product(request, pk):
    vendor_product = get_object_or_404(VendorProduct, pk=pk)

    if request.method == "POST":
        form = VendorProductForm(request.POST, instance=vendor_product)
        if form.is_valid():
            vendor_product = form.save(commit=False)
            vendor_product.user = request.user
            vendor_product.published_date = timezone.now()
            vendor_product.save()
            return redirect('product_details', pk=vendor_product.pk)
    else:
        form = VendorProductForm(instance=vendor_product)

    return render(request, 'vendor_products/edit.html', {'form': form})


def delete_vendor_product(request, pk):
    vendor_product = get_object_or_404(VendorProduct, pk=pk)
    vendor_product.delete()
    return redirect('vendor_product_list')