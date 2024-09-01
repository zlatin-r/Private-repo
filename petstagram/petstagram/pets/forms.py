from django import forms

from petstagram.pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet

        fields = ("name", "pet_photo", "date_of_birth")
