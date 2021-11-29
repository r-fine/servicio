from django import forms
from django.db import models
from django import forms

from .models import Category


class CategoryCreationForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'slug', 'parent', 'description', 'image']
