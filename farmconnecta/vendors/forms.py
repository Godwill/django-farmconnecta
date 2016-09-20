from django import forms
from models import Vendors


class VendorsForm(forms.ModelForm):

    class Meta:
        model = Vendors
        fields = ('name', 'latitude', 'longitude', 'description', 'images')