from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxLengthValidator, MaxValueValidator
"""Forms of the project."""

# Create your forms here.
class ThingForm (forms.ModelForm):
   class Meta:
      model = Thing
      fields = ['name', 'description', 'quantity']
      widgets = {
         'description' : forms.Textarea(),
         'quantity' : forms.NumberInput()
      }