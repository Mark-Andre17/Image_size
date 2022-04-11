from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ImageSerializer
from main.models import Picture


class CreateListDestroyViewSet(mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    pass


NO_FIELD = {'status': 'Заполни хоть одно поле'}


class ImageViewSet(CreateListDestroyViewSet):
    queryset = Picture.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        if not request.data:
            return Response(NO_FIELD, status.HTTP_400_BAD_REQUEST)
        if 'url' in request.data and 'file' in request.data:
            return Response(
                {'__all__': 'Нельзя так делать'},
                status.HTTP_400_BAD_REQUEST
            )

        serializer = ImageSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True)
    def resize(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not serializer.validated_data:
            return Response(NO_FIELD, status.HTTP_400_BAD_REQUEST)
        image = get_object_or_404(Picture, pk=pk)
        width = serializer.validated_data.get('width')
        height = serializer.validated_data.get('height')
        new_image_file, image_name = Picture.resize_image(image, width, height)
        serializer.save(
            picture=new_image_file, name=image_name, width=width,
            height=height, parent_picture=image
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
