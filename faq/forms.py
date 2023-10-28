from django import forms
from .models import FAQEntry


class FAQForm(forms.ModelForm):

    class Meta:
        model = FAQEntry
        fields = ('question', 'answer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
