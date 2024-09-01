from django.shortcuts import render, redirect

from petstagram.pets.forms import PetEditForm, PetBaseForm
from petstagram.pets.models import Pet


# Create your views here.
def create_pet(request):
    pet_form = PetBaseForm(request.POST or None)

    if request.method == 'POST':
        if pet_form.is_valid():
            created_pet = pet_form.save()
            return redirect("details pet", username="admin", pet_slug=created_pet.slug)

    context = {
        "pet_form": pet_form,
    }
    return render(request, "pets/pet-add-page.html", context)


def details_pet(request, username, pet_slug):
    context = {
        "pet": Pet.objects.get(slug=pet_slug),
    }
    return render(request, "pets/pet-details-page.html", context)


def edit_pet(request, username, pet_slug):
    pet_form = PetBaseForm()

    if request.method == 'POST':
        if pet_form.is_valid():
            updated_pet = pet_form.save()
            return redirect("details pet", username=username, pet_slug=pet_slug)

    context = {
        "pet_form": pet_form,
    }
    return render(request, "pets/pet-edit-page.html", context)


def delete_pet(request, username, pet_slug):
    context = {}
    return render(request, "pets/pet-delete-page.html", context)
