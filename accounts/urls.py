from django.urls import path
from .views.admin import (
    StaffListView,
    staff_activate,
    staff_delete,
    CategoryFormView
)
from .views.staff import (
    RegisterStaffView,
    dashboard_staff,
    staff_form,
)
app_name = 'accounts'

urlpatterns = [
    path(
        "admin-dashboard/",
        StaffListView.as_view(), name='staff_table'),
    # path(
    #     'register-staff/',
    #      staff.register_staff, name='register_staff'
    # ),
    path(
        'register-staff/',
        RegisterStaffView.as_view(), name='register_staff'
    ),
    path(
        'staff-dashboard/',
        dashboard_staff, name='dashboard_staff'
    ),
    # path(
    #     'admin-dashboard/',
    #      admin.dashboard_admin, name='dashboard_admin'
    # ),
    path(
        'staff-form/<int:staff_id>/',
        staff_form, name='staff_form'
    ),
    path(
        'staff-delete/<int:staff_id>/',
        staff_delete, name='staff_delete'
    ),
    path(
        'staff-activate/<int:staff_id>/',
        staff_activate, name='staff_activate'
    ),
    path(
        'admin/add-category/',
        CategoryFormView.as_view(), name='add_category'
    )
]
