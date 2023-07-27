from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import exceptions as rest_exceptions
from rest_framework.views import APIView, Response
from .models import Property, ProPertyDescriptions, ProPertyImages
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
                          "created_date": new_property.created_date,
                        "modified_date": new_property.modified_date
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
