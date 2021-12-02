from django.urls import path
from .views import (
    HomeView,
    CategoryListView,
    CategoryDetailView,
)

app_name = 'services'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all-category/', CategoryListView.as_view(), name='all_category'),
    path('<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),

]
