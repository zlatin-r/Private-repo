from django import forms

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet

        fields = ("name", "date_of_birth", "pet_photo",)


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass
