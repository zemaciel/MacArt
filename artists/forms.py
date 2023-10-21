from django import forms
from .models import Artist, SocialMedia

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        exclude = ('artist',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'