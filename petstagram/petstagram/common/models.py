from django.db import models

from petstagram.photos.models import Photo


# Create your models here.

class Comment(models.Model):
    text = models.TextField(
        max_length=300,
    )
    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.RESTRICT
    )


class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.RESTRICT
    )
