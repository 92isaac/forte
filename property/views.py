from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import exceptions as rest_exceptions
from rest_framework.views import APIView, Response
from .models import Property, ProPertyDescriptions, ProPertyImages, SingleImage
from . import serializers

# Create your views here.

class ProperyList(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = serializers.PropertySerializer


class CreateProperty(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = serializers.PropertySerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            try:
                new_property = serializer.create(serializer.validate_data)
                return Response({
                    "status": True, "message": "Property created successfully",
                    "data":{
                        "id":new_property.id, 
                        "title": new_property.title,
                        "location": new_property.location,
                        "price": new_property.price,
                        "number_of_rooms": new_property.number_of_rooms,
                        "number_of_bath": new_property.number_of_bath,
                        "property_size": new_property.property_size,
                        "single_image": new_property.single_image,
                        "property_images": new_property.property_images,
                        "created_date": new_property.created_date,
                        "modified_date": new_property.modified_date,
                    }
                }, status=status.HTTP_201_CREATED)
            except Exception:
                return Response({
                    'status': False,
                    'message': 'Property Creation failed! Something went wrong.',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except rest_exceptions.ValidationError:
            return Response({
                'status': False,
                'message': 'Property already Exist! ' \
                    'Or invalid email address.',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'status': False,
                'message': 'Subscription failed! Unknown error ocurred.',
                'data': {}
            }, status=status.HTTP_400_BAD_REQUEST)


class UpdateProperty(generics.UpdateAPIView):

    queryset = Property.objects.all()
    serializer_class = serializers.PropertySerializer

    def update(self, request, *args, **kwargs):

        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exceptions=True)
            try:
                edit_property = generics._get_object_or_404(Property, pk=self.kwargs['pk'])
                edit_property.title = serializer.validate_data['title']
                edit_property.location = serializer.validate_data['location']
                edit_property.price = serializer.validate_data['price']
                edit_property.number_of_rooms = serializer.validate_data['number_of_rooms']
                edit_property.number_of_bath = serializer.validate_data['number_of_bath']
                edit_property.property_size = serializer.validate_data['property_size']
                edit_property.single_image = serializer.validate_data['single_image']
                edit_property.property_images = serializer.validate_data['property_images']
                edit_property.save()
                return Response({
                    "status": True,
                    "message": "Property Updated Successfully",
                    "data":{
                         "id":edit_property.id, 
                        "title": edit_property.title,
                        "location": edit_property.location,
                        "price": edit_property.price,
                        "number_of_rooms": edit_property.number_of_rooms,
                        "number_of_bath": edit_property.number_of_bath,
                        "property_size": edit_property.property_size,
                        "single_image": edit_property.single_image,
                        "property_images": edit_property.property_images,
                        "created_date": edit_property.created_date,
                        "modified_date": edit_property.modified_date,
                    }
                }, status=status.HTTP_200_OK)
            except (Property.DoesNotExist, generics.Http404):
                return Response({
                    'status': False,
                    'message': 'Property with matching details not found',
                    'data': serializer.errors
                }, status=status.HTTP_404_NOT_FOUND)
        except rest_exceptions.ValidationError:
            return Response({
                'status': False,
                'message': 'Invalid details provided! ' \
                    'Or invalid field detected.',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'status': False,
                'message': 'Property update failed! Unknown error ocurred.',
                'data': {}
            }, status=status.HTTP_400_BAD_REQUEST)


class DeleteProppertyView(generics.DestroyAPIView):
    """Delete Matched Property From Database"""

    queryset = Property.objects.all()
    serializer_class = serializers.PropertySerializer




# single image
class SingleImageList(generics.ListAPIView):
    queryset = SingleImage.objects.all()
    serializer_class = serializers.SingleImageSerializer


class CreateSingleImage(generics.CreateAPIView):
    queryset = SingleImage.objects.all()
    serializer_class = serializers.SingleImageSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            try:
                single_image = serializer.create(serializer.validate_data)
                return Response({
                    "status": True, "message": "Property created successfully",
                    "data":{
                        "id":single_image.id, 
                        "single_image_url": single_image.single_image_url,
                          "created_date": single_image.created_date,
                        "modified_date": single_image.modified_date
                    }
                }, status=status.HTTP_201_CREATED)
            except Exception:
                return Response({
                    'status': False,
                    'message': 'Property images Creation failed! Something went wrong.',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except rest_exceptions.ValidationError:
            return Response({
                'status': False,
                'message': 'Property image already Exist! ' \
                    'Or invalid email address.',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'status': False,
                'message': 'Unknown error ocurred.',
                'data': {}
            }, status=status.HTTP_400_BAD_REQUEST)









# property images

class PropertImageList(generics.ListAPIView):
    queryset = ProPertyImages.objects.all()
    serializer_class = serializers.ProPertyImagesSerializer


class CreatePropertyImage(generics.CreateAPIView):
    queryset = ProPertyImages.objects.all()
    serializer_class = serializers.ProPertyImagesSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            try:
                new_property_image = serializer.create(serializer.validate_data)
                return Response({
                    "status": True, "message": "Property created successfully",
                    "data":{
                        "id":new_property_image.id, 
                        "gallery": new_property_image.gallery,
                          "created_date": new_property_image.created_date,
                        "modified_date": new_property_image.modified_date
                    }
                }, status=status.HTTP_201_CREATED)
            except Exception:
                return Response({
                    'status': False,
                    'message': 'Property images Creation failed! Something went wrong.',
                    'data': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except rest_exceptions.ValidationError:
            return Response({
                'status': False,
                'message': 'Property image already Exist! ' \
                    'Or invalid email address.',
                'data': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({
                'status': False,
                'message': 'Unknown error ocurred.',
                'data': {}
            }, status=status.HTTP_400_BAD_REQUEST)