from django.urls import path, include
from petstagram.pets.views import PetCreateView, delete_pet, PetDetailsView, PetEditView

urlpatterns = (
    path("add/", PetCreateView.as_view(), name="add pet"),
    path("<str:username>/pet/<slug:pet_slug>/",
         include([
             path("", PetDetailsView.as_view(), name="details pet"),
             path("edit/", PetEditView.as_view(), name="edit pet"),
             path("delete/", delete_pet, name="delete pet"),
             ])
         )
)
