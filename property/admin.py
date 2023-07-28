from django.contrib import admin
from .models import Property, ProPertyImages, MultipleImage, SingleImage
# Register your models here.

admin.site.register([Property, ProPertyImages, MultipleImage, SingleImage])