from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Write Here',
            }
        ),
        label='First Name',
        help_text='Texto de Ajuda',
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
        widgets = {
            ...
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        return super().clean()