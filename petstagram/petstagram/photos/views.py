from django.shortcuts import render

from petstagram.photos.models import Photo


# Create your views here.
def add_photo(request):
    return render(request, "photos/photo-add-page.html")


def details_photo(request, pk):
    context = {
        "pet_photo": Photo.objects.get(pk=pk),
    }
    return render(request, "photos/photo-details-page.html", context)


def edit_photo(request, pk):
    return render(request, "photos/photo-edit-page.html")
