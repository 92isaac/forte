from django.db import models
import uuid
import json
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField
from django.contrib.postgres.fields import ArrayField


class BaseModel(models.Model):
    """Defines common model fields like id, created and modified date, etc."""

    id = models.CharField(
        _('Unique ID'), max_length=255, primary_key=True, default=uuid.uuid4,
        editable=False, help_text=_("Model unique identifier")
    )
    created_date = models.DateTimeField(
        _("date created"), auto_now_add=True,
        help_text=_("Date and time of creation")
    )
    modified_date = models.DateTimeField(
        _("date modified"), auto_now=True,
        help_text=_("Date and time last modified")
    )

    class Meta:
        abstract =True


class SingleImage(BaseModel):
    image = CloudinaryField("image", default='https://via.placeholder.com/350x150')

    @property
    def single_image_url(self):
        return f"https://res.cloudinary.com/dpoix2ilz/{self.image}"
    

class MultipleImage(BaseModel):
    """Represent multiply image for a property"""

    multimage = CloudinaryField("image", default='https://via.placeholder.com/350x150')

    @property
    def image_url(self):
        return f"https://res.cloudinary.com/dpoix2ilz/{self.multimage}"
    

class ProPertyDescriptions(BaseModel):
    description = ArrayField(models.TextField())


class ProPertyImages(BaseModel):
    gallery = models.ForeignKey(MultipleImage, blank=True, on_delete=models.CASCADE, null=True, related_name='property_images')





class Property(BaseModel):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_rooms = models.PositiveIntegerField()
    number_of_bath = models.PositiveIntegerField()
    property_size = models.DecimalField(max_digits=10, decimal_places=2)




    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_date", "title")







