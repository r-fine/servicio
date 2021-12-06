from django.urls import path
from .views.auth import RegisterStaffView
from .views.user import (
    user_dashboard,
    order_history,
    cancel_order,
)
from .views.admin import (
    StaffListView,
    staff_activate,
    staff_delete,
    CategoryCreateView,
    ServiceCreateView,
)
from .views.staff import (
    dashboard_staff,
    staff_form,
)
app_name = 'accounts'

urlpatterns = [
    ######################### FOR STAFF #########################
    path("admin-dashboard/", StaffListView.as_view(), name='staff_table'),
    path('register-staff/', RegisterStaffView.as_view(), name='register_staff'),
    path('staff-dashboard/',  dashboard_staff, name='dashboard_staff'),
    path('staff-form/<int:staff_id>/', staff_form, name='staff_form'),

    ######################### FOR ADMIN #########################
    path('staff-delete/<int:staff_id>/', staff_delete, name='staff_delete'),
    path(
        'staff-activate/<int:staff_id>/', staff_activate, name='staff_activate'
    ),
    path('admin/add-category/', CategoryCreateView.as_view(), name='add_category'),
    path('admin/add-service/', ServiceCreateView.as_view(), name='add_service'),

    ######################### FOR USER #########################
    path('user/user-dashboard', user_dashboard, name='user_dashboard'),
    path('user/user-dashboard', user_dashboard, name='user_dashboard'),
    path('user/order-history', order_history, name='order_history'),
    path(
        'user/cancel-order/<int:order_id>/', cancel_order, name='cancel_order'
    ),
]
