from django import forms
from models import VendorProduct


class VendorProductForm(forms.ModelForm):

    class Meta:
        model = VendorProduct
        fields = ('title', 'vendor', 'category', 'price', 'description', 'images')