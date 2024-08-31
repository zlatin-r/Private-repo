from django.shortcuts import render

from petstagram.photos.models import Photo


# Create your views here.


def index(request):
    context = {
        "pet_photos": Photo.objects.all()
    }
    return render(request, "common/index.html", context)
