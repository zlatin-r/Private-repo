from audioop import reverse

from django.shortcuts import render, redirect
from django.views import generic as views
from petstagram.pets.forms import PetEditForm, PetCreateForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.
# def create_pet(request):
#     pet_form = PetCreateForm(request.POST or None)
#
#     if request.method == 'POST':
#         if pet_form.is_valid():
#             created_pet = pet_form.save()
#             return redirect("details pet", username="admin", pet_slug=created_pet.slug)
#
#     context = {
#         "pet_form": pet_form,
#     }
#     return render(request, "pets/pet-add-page.html", context)


class PetCreateView(views.CreateView):
    # model = Pet
    # fields = ("name", "date_of_birth", "pet_photo",)

    form_class = PetCreateForm
    template_name = "pets/pet-add-page.html"

    def get_success_url(self):
        return reverse("details pet", kwargs={"username": "admin", "pet_slug": self.object.slug})


# def details_pet(request, username, pet_slug):
#     context = {
#         "pet": Pet.objects.get(slug=pet_slug),
#     }
#     return render(request, "pets/pet-details-page.html", context)

class PetDetailsView(views.DetailView):
    model = Pet
    template_name = "pets/pet-details-page.html"
    slug_url_kwarg = "pet_slug"


# def edit_pet(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug).get()
#     pet_form = PetEditForm(request.POST or None, instance=pet)
#
#     if request.method == 'POST':
#         if pet_form.is_valid():
#             updated_pet = pet_form.save()
#             return redirect("details pet", username=username, pet_slug=pet_slug)
#
#     context = {
#         "pet_form": pet_form,
#         "username": username,
#         "pet": pet,
#     }
#     return render(request, "pets/pet-edit-page.html", context)


class PetEditView(views.UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = "pets/pet-edit-page.html"
    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)

        contex["username"] = "admin"
        return contex


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    pet_form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        pet_form.save()
        return redirect("index")

    context = {
        "pet_form": pet_form,
        "username": username,
        "pet": pet,
    }

    return render(request, "pets/pet-delete-page.html", context)
