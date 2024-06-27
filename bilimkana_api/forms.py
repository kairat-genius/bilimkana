import base64
from django import forms

class ImgModelForm(forms.ModelForm):
    image = forms.ImageField(label='Upload Image', required=False)

    def save(self, commit=True):
        instance = super().save(commit=False)
        image_file = self.cleaned_data.get('image')

        if image_file:
            instance.img = base64.b64encode(image_file.read()).decode('utf-8')

        if commit:
            instance.save()
        return instance
