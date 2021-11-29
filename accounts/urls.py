from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path("admin-dashboard/",
         views.StaffListView.as_view(), name='table_admin'),
    # path('register-staff/',
    #      views.register_staff, name='register_staff'),
    path('register-staff/',
         views.RegisterStaffView.as_view(), name='register_staff'),
    path('staff-dashboard/',
         views.dashboard_staff, name='dashboard_staff'),
    # path('admin-dashboard/',
    #      views.dashboard_admin, name='dashboard_admin'),
    path('staff-form/<int:staff_id>/',
         views.staff_form, name='staff_form'),
    path('staff-delete/<int:staff_id>/',
         views.staff_delete, name='staff_delete'),
    path('staff-activate/<int:staff_id>/',
         views.staff_activate, name='staff_activate'),
]
