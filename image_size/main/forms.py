from django import forms
from django.forms import ModelForm
from .models import Picture


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['name', 'picture', 'url']

    def clean(self):
        if not self.cleaned_data.get('url') and not self.cleaned_data.get('picture'):
            raise forms.ValidationError('Надо заполнить хотя бы одно поле')
        if self.cleaned_data.get('url') and self.cleaned_data.get('picture'):
            raise forms.ValidationError('Надо заполнить только одно поле')
        if self.cleaned_data.get('url'):
            picture = Picture.save_img_from_url(self.cleaned_data.get('url'))
            self.cleaned_data['picture'] = picture
        return self.cleaned_data


class ResizeForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['width', 'height']

    def clean(self):
        if not self.cleaned_data.get('width') and not self.cleaned_data.get('height'):
            raise forms.ValidationError('Заполните хотя бы одно поле')
        return self.cleaned_data
