from django import forms
from django.core.exceptions import ValidationError

class EditWordlistForm(forms.Form):
    name = forms.CharField(help_text="Enter the name of the list.")

    def clean_name(self):
        name = self.cleaned_data['name']

        # Check if a date is not in the past.
        if len(name) < 3:
            raise ValidationError('Invalid name - shorter than 3 characters')

        # Check if a date is in the allowed range (+4 weeks from today).
        if len(name) > 40:
            raise ValidationError('Invalid name - longer than 20 characters')

        # Remember to always return the cleaned data.
        return name