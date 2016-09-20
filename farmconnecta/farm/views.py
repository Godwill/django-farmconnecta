from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from forms import FarmForm
from .models import Farm


# Create your views here.
def farm_list(request):
    farms = Farm.objects.filter().order_by('published_date')
    print farms
    return render(request, 'farms/index.html', {'farms': farms})


def new_farm(request):

    if request.method == 'POST':
        form = FarmForm(request.POST, request.FILES)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.user = request.user
            farm.published_date = timezone.now()
            farm.save()
            return redirect('farm_details', pk=farm.pk)

    else:
        form = FarmForm

    return render(request, 'farms/create.html', {'form': form})


def farm_details(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    products = farm.product_set.all()
    print products
    return render(request, 'farms/farm.html', {'farm': farm, 'products': products})


def edit_farm(request, pk):
    farm = get_object_or_404(Farm, pk=pk)

    if request.method == "POST":
        form = FarmForm(request.POST, instance=farm)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.user = request.user
            farm.published_date = timezone.now()
            farm.save()
            return redirect('farm_details', pk=farm.pk)
    else:
        form = FarmForm(instance=farm)

    return render(request, 'farms/edit.html', {'form': form})


def delete_farm(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    farm.delete()
    return redirect('/')