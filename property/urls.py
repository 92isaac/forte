from django.urls import path
from . import views

urlpatterns =[
    # Links associated with properties
    path('properties/', views.ProperyList.as_view(), name='properties'),
    path('properties/add/', views.CreateProperty.as_view(), name='add-property'),
    path('properties/update/<pk>/', views.UpdateProperty.as_view(), name='update-property'),
    path('properties/delete/<pk>/', views.DeleteProppertyView.as_view(), name='delete-property'),

    # Link to all image uploaded for gallery
    path('properties_images/', views.PropertImageList.as_view(), name='properties_images'),
    path('properties_images/add/', views.CreatePropertyImage.as_view(), name='add_properties_images'),

    # links to all single images
    path('single_images/', views.SingleImageList.as_view(), name='single_image'),
    path('single_images/add/', views.CreateSingleImage.as_view(), name='add_single_image'),
]