from django.urls import path
from .views import (
    HomeView,
    CategoryListView,
    CategorySingleView,
    # submit_review,
)

app_name = 'services'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all-category/', CategoryListView.as_view(), name='all_category'),
    path('<slug:slug>/', CategorySingleView.as_view(), name='category_detail'),
    # path('submit_review/<int:category_id>/',
    #      submit_review, name='submit_review'),

]
