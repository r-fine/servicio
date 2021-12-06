from django import forms

from .models import Category, Service, ReviewRating


class CategoryCreationForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'parent', 'description', 'image']


class ServiceCreationForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['category', 'name', 'summary', 'notes', 'image', 'is_active']


class ReviewRatingForm(forms.ModelForm):

    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
