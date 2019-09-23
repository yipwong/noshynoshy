from django.db import models
import uuid


class Picture(models.Model):
    image = models.ImageField(upload_to="gallery")
    caption = models.CharField(max_length=100)
    owner = models.CharField(max_length=60)

    def __str__(self):
        return self.caption


class Image(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    created_at = models.DateTimeField(auto_now_add=True)
    caption = models.CharField(max_length=100)
    owner = models.CharField(max_length=60)
    image = models.FileField()
