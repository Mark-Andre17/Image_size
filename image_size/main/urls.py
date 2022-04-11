from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('load_picture/', LoadPicture.as_view(), name='load_picture'),
    path('resize_picture/', pictures, name='pictures'),
    path('resize_picture/<int:pk>/', ResizePicture.as_view(), name='resize_picture'),
]
