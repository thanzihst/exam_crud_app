from django import forms

from store.models import RealEstate


class RealEstateCreateForm(forms.ModelForm):

    class Meta:

        model=RealEstate

        fields="__all__"

        