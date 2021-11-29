from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django_tables2 import SingleTableView

from accounts.models import LocalUser, Staff
from .forms import RegisterStaffForm, StaffEditForm
from .tables import StaffTable


class StaffListView(SingleTableView):
    model = Staff
    table_class = StaffTable
    template_name = "admin/admin-dashboard.html"

    def form_valid(self, form):
        # email = form.instance.email
        form.instance.username = self.request.user_email.split("@")[0]
        return super().form_valid(form)


class RegisterStaffView(SuccessMessageMixin, CreateView):
    template_name = 'staff/register-staff.html'
    success_url = reverse_lazy('account_login')
    form_class = RegisterStaffForm
    success_message = "Profile Created"


# def register_staff(request):
#     userForm = RegisterStaffForm()
#     staffForm = StaffEditForm()

#     if request.method == 'POST':
#         userForm = RegisterStaffForm(request.POST)
#         staffForm = StaffEditForm(request.POST, request.FILES)
#         if userForm.is_valid() and staffForm.is_valid():
#             user = userForm.save()
#             user.set_password(user.password)
#             user.save()
#             staff = staffForm.save(commit=False)
#             staff.user = user
#             staff.save()

#             return redirect('accounts:dashboard_staff')
#     else:
#         userForm = RegisterStaffForm()
#         staffForm = StaffEditForm()
#         context = {'userForm': userForm, 'staffForm': staffForm}

#         return render(request, 'staff/register-staff.html', context)


def dashboard_staff(request):
    staff = Staff.objects.get(user=request.user)
    if staff.is_active:
        return HttpResponse('Staff Dashboard')
    else:
        return redirect('accounts:staff_edit', staff.id)


# def dashboard_admin(request):

#     return HttpResponse('Dashboard Admin')

def staff_form(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)

    if request.method == 'POST':
        form = StaffEditForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            # staff = form.save(commit=False)
            # staff.is_active = True
            staff.save()
            if request.user.is_superuser:
                return redirect('accounts:table_admin')
            return redirect('accounts:dashboard_staff')
        else:
            return HttpResponse('failed to submit')
    else:
        form = StaffEditForm(instance=staff)
        context = {'form': form}

        return render(request, 'staff/staff-form.html', context)


def staff_delete(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    user = LocalUser.objects.get(pk=staff.user_id)
    user.delete()

    return redirect('accounts:table_admin')


def staff_activate(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    if staff.is_active:
        staff.is_active = False
    else:
        staff.is_active = True
    staff.save()

    return redirect('accounts:table_admin')
