from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, FormView

from .forms import *

menu = [
    {'title': 'Загрузить изображение', 'url_name': 'load_picture'},
    {'title': 'Изменить размер изображения', 'url_name': 'resize_picture'}
]


def home(request):
    context = {'title': 'Главная страница', 'menu': menu}
    return render(request, 'main/main.html', context)


def pictures(request):
    images = Picture.objects.all()
    context = {'title': 'Все изображения', 'images': images}
    return render(request, 'main/all_pictures.html', context)


class LoadPicture(CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'main/load_picture.html'

    def get_success_url(self):
        return reverse('home')


class ResizePicture(FormView):
    form_class = ResizeForm
    template_name = 'main/resize_picture.html'

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = get_object_or_404(Picture, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        resized_image = form.save(commit=False)
        image = get_object_or_404(Picture, pk=self.kwargs['pk'])
        width = form.cleaned_data.get('width')
        height = form.cleaned_data.get('height')
        new_image_file, image_name = Picture.resize_image(image, width, height)
        resized_image.parent_picture = image
        resized_image.width = width
        resized_image.height = height
        resized_image.picture = new_image_file
        resized_image.name = image_name
        resized_image.save()
        return super().form_valid(form)
