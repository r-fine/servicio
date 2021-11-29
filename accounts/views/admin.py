from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from django_tables2 import SingleTableView

from accounts.models import LocalUser, Staff
from accounts.tables import StaffTable
from services.forms import CategoryCreationForm
from services.models import Category


class StaffListView(SingleTableView):
    model = Staff
    table_class = StaffTable
    template_name = "admin/admin-dashboard.html"

    def form_valid(self, form):
        # email = form.instance.email
        form.instance.username = self.request.user_email.split("@")[0]
        return super().form_valid(form)


# def dashboard_admin(request):

#     return HttpResponse('Dashboard Admin')


def staff_delete(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    user = LocalUser.objects.get(pk=staff.user_id)
    user.delete()

    return redirect('accounts:staff_table')


def staff_activate(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    if staff.is_active:
        staff.is_active = False
    else:
        staff.is_active = True
    staff.save()

    return redirect('accounts:staff_table')


class CategoryFormView(SuccessMessageMixin, CreateView):
    template_name = 'admin/create-category.html'
    form_class = CategoryCreationForm
    success_url = reverse_lazy('accounts:add_category')
    success_message = "A new category has been added"

    # def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.

    # return super().form_valid(form)
