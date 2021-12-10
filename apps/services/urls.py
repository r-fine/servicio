from django.urls import path
from .views import (
    HomeView,
    CategoryListView,
    category_list,
    CategorySingleView,
    # submit_review,
)

app_name = 'services'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all-category/', CategoryListView.as_view(), name='all_category'),
    path('<slug:slug>/', CategorySingleView.as_view(), name='category_detail'),
    path(
        'categories/<slug:category_slug>/', category_list, name='category_list'
    ),
    # path('submit_review/<int:category_id>/',
    #      submit_review, name='submit_review'),

]
