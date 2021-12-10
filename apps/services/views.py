from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import FormView
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import *
from .forms import ReviewRatingForm

from apps.orders.models import Order, OrderItem


class HomeView(ListView):
    model = Category
    template_name = 'service/home.html'
    context_object_name = 'subcategories'
    paginate_by = 4
    queryset = Category.objects.filter(level=1)


class CategoryListView(ListView):
    model = Category
    template_name = "service/category-list.html"


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    subcategories = Category.objects.filter(parent=category)
    return render(request, 'service/category_list.html', {'category': category, 'subcategories': subcategories})


class CategoryDetailView(DetailView):
    model = Category
    template_name = "service/category-detail.html"
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'services': Service.objects.filter(category=self.object),
            'ordered': OrderItem.objects.filter(user=self.request.user, service__in=Service.objects.filter(category=self.object), is_ordered=True, order__in=Order.objects.filter(is_ordered=True))
            if self.request.user.is_authenticated else None,
            'reviews': ReviewRating.objects.filter(
                category_id=self.object.id,
                status=True
            ),
            'is_reviewed': ReviewRating.objects.get(user=self.request.user, category=self.object)
            if (self.request.user.is_authenticated and ReviewRating.objects.filter(category_id=self.object.id, status=True).exists()) else None,
            'form': ReviewRatingForm(),
        })
        return context


class ReviewRatingFormView(LoginRequiredMixin, SuccessMessageMixin, SingleObjectMixin, FormView):
    template_name = "service/category-detail.html"
    model = Category
    success_message = 'Thank you! Your review has been submitted.'

    def get_form(self):
        try:
            reviews = ReviewRating.objects.get(
                user=self.request.user, category=self.object
            )
            return ReviewRatingForm(self.request.POST, instance=reviews)
        except ReviewRating.DoesNotExist:
            return ReviewRatingForm(self.request.POST)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('services:category_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.category = self.object
        form.instance = form.save()

        return super().form_valid(form)


class CategorySingleView(View):

    def get(self, request, *args, **kwargs):
        view = CategoryDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReviewRatingFormView.as_view()
        return view(request, *args, **kwargs)
