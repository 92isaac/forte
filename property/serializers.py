from rest_framework import serializers
from .models import Property, ProPertyImages, ProPertyDescriptions, SingleImage, MultipleImage


class SingleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleImage
        fields =('id', 'single_image_url', 
                 'created_date',
                 'modified_date')
        read_only_fields = (
            'id', 'created_date', 'modified_date'
        )

class MultipleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleImage
        fields =('id', 'image_url', 
                 'created_date',
                 'modified_date')
        read_only_fields = (
            'id', 'created_date', 'modified_date'
        )




class ProPertyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProPertyImages
        fields=('id', 'gallery',
                'created_date',
                 'modified_date')
        read_only_fields = (
            'id', 'created_date', 'modified_date'
        )

class ProPertyDescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProPertyDescriptions
        fields =('id', 'description', 
                 'created_date',
                 'modified_date')
        read_only_fields = (
            'id', 'created_date', 'modified_date'
        )

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields =('id', 'title', 
                 'location','price',
                 'number_of_rooms',
                 'number_of_bath',
                 'property_size',
                 'single_image',
                 'property_images',
                 'created_date',
                 'modified_date')
        read_only_fields = (
            'id', 'created_date', 'modified_date'
        )