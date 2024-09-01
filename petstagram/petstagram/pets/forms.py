from django import forms
from django.core.exceptions import ValidationError

from petstagram.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet

        fields = ("name", "date_of_birth", "pet_photo",)

        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Pet name'}),
            "date_of_birth": forms.DateInput(attrs={'type': 'date'}),
            "pet_photo": forms.URLInput(attrs={'placeholder': 'Link to image'}),
        }

        labels = {
            "name": "Pet name",
            "pet_photo": "Link to image",
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["date_of_birth"].widget.attrs["readonly"] = "readonly"

    def clean_date_of_birth(self):  # Validate date_of_birth
        date_of_birth = self.cleaned_data["date_of_birth"]

        if date_of_birth != self.instance.date_of_birth:
            raise ValidationError("Date of birth is readonly")

        return date_of_birth
