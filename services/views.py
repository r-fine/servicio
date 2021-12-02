from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from allauth.account.decorators import verified_email_required

from .models import *


class HomeView(ListView):
    model = Category
    template_name = 'service/home.html'
    context_object_name = 'subcategories'
    paginate_by = 4
    queryset = Category.objects.filter(level=1)


class CategoryListView(ListView):
    model = Category
    template_name = "service/category-list.html"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "service/category-detail.html"
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'services': Service.objects.filter(category=self.object)
        })
        return context
