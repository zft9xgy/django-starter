from django import forms
from notes.models import Tag
from django.core.exceptions import ValidationError

class TagFormAdmin(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'slug']

    # def clean_slug(self):
    #     data = self.cleaned_data["slug"]
        
    #     raise ValidationError("Validation Error message")

    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     return data