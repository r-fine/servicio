from django import forms
from django.db import models
from django import forms
from django.forms import fields

from .models import Category, Service


class CategoryCreationForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'parent', 'description', 'image']


class ServiceCreationForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['category', 'name', 'summary', 'notes', 'image', 'is_active']
