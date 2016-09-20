from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from forms import VendorsForm
from .models import Vendors


# Create your views here.
def vendor_list(request):
    vendors = Vendors.objects.filter().order_by('published_date')
    print vendors
    return render(request, 'vendors/index.html', {'vendors': vendors})


def new_vendor(request):

    if request.method == 'POST':
        form = VendorsForm(request.POST, request.FILES)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = request.user
            vendor.published_date = timezone.now()
            vendor.save()
            return redirect('vendor_details', pk=vendor.pk)

    else:
        form = VendorsForm

    return render(request, 'vendors/create.html', {'form': form})


def vendor_details(request, pk):
    vendor = get_object_or_404(Vendors, pk=pk)
    products = vendor.vendorproduct_set.all()
    print products
    return render(request, 'vendors/vendor.html', {'vendor': vendor, 'products': products})
    # return render(request, 'vendors/vendor.html', {'vendor': vendor})


def edit_vendor(request, pk):
    vendor = get_object_or_404(Vendors, pk=pk)

    if request.method == "POST":
        form = VendorsForm(request.POST, instance=vendor)
        if form.is_valid():
            vendor = form.save(commit=False)
            vendor.user = request.user
            vendor.published_date = timezone.now()
            vendor.save()
            return redirect('vendor_details', pk=vendor.pk)
    else:
        form = VendorsForm(instance=vendor)

    return render(request, 'vendors/edit.html', {'form': form})


def delete_vendor(request, pk):
    vendor = get_object_or_404(Vendors, pk=pk)
    vendor.delete()
    return redirect('/')