from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


from accounts.models import LocalUser, Staff
from accounts.forms import RegisterStaffForm, StaffEditForm


class RegisterStaffView(SuccessMessageMixin, CreateView):
    template_name = 'staff/register-staff.html'
    form_class = RegisterStaffForm
    success_url = reverse_lazy('account_login')
    success_message = "Profile Created"


def staff_form(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)

    if request.method == 'POST':
        form = StaffEditForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            # staff = form.save(commit=False)
            # staff.is_active = True
            staff.save()
            if request.user.is_superuser:
                return redirect('accounts:staff_table')
            return redirect('accounts:dashboard_staff')
        else:
            return HttpResponse('failed to submit')
    else:
        form = StaffEditForm(instance=staff)
        context = {'form': form}

        return render(request, 'staff/staff-form.html', context)


def dashboard_staff(request):
    staff = Staff.objects.get(user=request.user)
    if staff.is_active:
        return HttpResponse('Staff Dashboard')
    else:
        return redirect('accounts:staff_form', staff.id)


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
