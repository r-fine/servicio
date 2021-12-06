from django.urls import path
from .views import (
    OrderCreateView,
    add_order,
    remove_item
)
app_name = 'orders'

urlpatterns = [
    path('place-order/', OrderCreateView.as_view(), name='order_create'),
    path('add-order/<int:service_id>/', add_order, name='add_order'),
    path(
        'remove-item/<int:service_id>/<int:order_item_id>/', remove_item, name='remove_item'
    ),
]
