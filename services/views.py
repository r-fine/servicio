from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test

from allauth.account.decorators import verified_email_required

from .models import *


# @verified_email_required
def home(request):
    categories = Category.objects.all()
    subcategories = Category.objects.filter(level=1)

    return render(request, 'home/home.html', {'categories': categories, 'subcategories': subcategories})


def category_details(request):
    pass
