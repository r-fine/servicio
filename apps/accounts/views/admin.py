from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.text import slugify

from django_tables2 import SingleTableView

from apps.accounts.models import LocalUser, Staff
from apps.accounts.tables import StaffTable
from apps.accounts.decorators import admin_required, admin_only
from apps.services.forms import CategoryCreationForm, ServiceCreationForm


# class AdminRequiredMixin(UserPassesTestMixin):
#     def test_func(self):
#         return self.request.user.is_superuser

@admin_required()
class StaffListView(SingleTableView):
    model = Staff
    table_class = StaffTable
    template_name = "admin/admin-dashboard.html"
    # table_data = Staff.objects.all()
    # paginator_class = LazyPaginator


# def dashboard_admin(request):

#     return HttpResponse('Dashboard Admin')

@admin_only
def staff_delete(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    user = LocalUser.objects.get(pk=staff.user_id)
    user.delete()

    return redirect('accounts:staff_table')


@admin_only
def staff_activate(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    if staff.is_active:
        staff.is_active = False
    else:
        staff.is_active = True
    staff.save()

    return redirect('accounts:staff_table')


@admin_required()
class CategoryCreateView(SuccessMessageMixin, CreateView):
    template_name = 'admin/create-category.html'
    form_class = CategoryCreationForm
    success_url = reverse_lazy('accounts:add_category')
    success_message = "A new category has been added"

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)

        return super().form_valid(form)


@admin_required()
class ServiceCreateView(SuccessMessageMixin, CreateView):
    template_name = 'admin/create-service.html'
    form_class = ServiceCreationForm
    success_url = reverse_lazy('accounts:add_service')
    success_message = "A new service has been added"
