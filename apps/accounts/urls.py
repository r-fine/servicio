from django.urls import path
from .views.auth import RegisterStaffView
from .views.user import (
    user_dashboard,
    order_history,
    cancel_order,
)
from .views.admin import (
    dashboard_admin,
    StaffTableView, staff_activate, staff_delete,
    CategoryServiceTableView,
    CategoryCreateView, edit_category, delete_category,
    ServiceCreateView, edit_service, delete_service,
    OrderTableView, OrderUpdateForm,
)
from .views.staff import (
    dashboard_staff,
    staff_form,
)
app_name = 'accounts'

urlpatterns = [

    ######################### FOR USER #########################
    path('user/user-dashboard', user_dashboard, name='user_dashboard'),
    path('user/user-dashboard', user_dashboard, name='user_dashboard'),
    path('user/order-history', order_history, name='order_history'),
    path(
        'user/cancel-order/<int:order_id>/', cancel_order, name='cancel_order'
    ),

    ######################### FOR STAFF #########################
    path('staff/register-staff/', RegisterStaffView.as_view(), name='register_staff'),
    path('staff/staff-dashboard/',  dashboard_staff, name='dashboard_staff'),
    path('staff/staff-form/<int:staff_id>/', staff_form, name='staff_form'),

    ######################### FOR ADMIN #########################
    path("admin/admin-dashboard/", dashboard_admin, name='dashboard_admin'),
    path("admin/staff-list/", StaffTableView.as_view(), name='staff_table'),
    path('admin/staff-delete/<int:staff_id>/',
         staff_delete, name='staff_delete'),
    path(
        'admin/staff-activate/<int:staff_id>/', staff_activate, name='staff_activate'
    ),
    path(
        'admin/product-list/', CategoryServiceTableView.as_view(), name='product_table'
    ),
    path('admin/category-add/', CategoryCreateView.as_view(), name='create_category'),
    path(
        'admin/category-edit/<int:category_id>/', edit_category, name='edit_category'
    ),
    path(
        'admin/category-delete/<int:category_id>/', delete_category, name='delete_category'
    ),
    path('admin/service-add/', ServiceCreateView.as_view(), name='create_service'),
    path(
        'admin/service-edit/<int:service_id>/', edit_service, name='edit_service'
    ),
    path(
        'admin/service-delete/<int:service_id>/', delete_service, name='delete_service'
    ),
    path(
        'admin/order-list/', OrderTableView.as_view(), name='order_table'
    ),
    path('admin/order-edit/<int:pk>/',
         OrderUpdateForm.as_view(), name='edit_order'),
]
