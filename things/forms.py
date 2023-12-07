from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxLengthValidator, MaxValueValidator
"""Forms of the project."""

# Create your forms here.
class ThingForm (forms.Form):
   class Meta:
      model = Thing
      fields = ['name', 'description', 'quantity']
      widgets = {
         'name' : forms.CharField(validators=[MaxLengthValidator(limit_value=35)]),
         'description' : forms.Textarea(),
         'quantity' : forms.NumberInput(validators=[MinValueValidator(limit_value=0), MaxValueValidator(limit_value=50)])
      }