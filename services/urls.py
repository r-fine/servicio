from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.category_details, name='category_details'),
]
