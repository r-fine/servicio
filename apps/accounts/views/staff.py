from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render
# from django.core.exceptions import PermissionDenied
from django.contrib import messages

from apps.accounts.models import Staff
from apps.accounts.forms import StaffEditForm
from apps.accounts.decorators import staff_only


@staff_only
def staff_form(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)

    if request.method == 'POST':
        form = StaffEditForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            # staff = form.save(commit=False)
            # staff.is_active = True
            staff.save()
            messages.success(request, 'Saved')
            if request.user.is_superuser:
                return redirect('accounts:staff_table')
            return redirect('accounts:dashboard_staff')
        else:
            return HttpResponse('failed to submit')
    else:
        form = StaffEditForm(instance=staff)
        try:
            activated = Staff.objects.get(user=request.user, is_active=True)
        except Staff.DoesNotExist:
            activated = None
        context = {'form': form, 'activated': activated}

        if request.user.is_superuser or staff.user.id == request.user.id:
            return render(request, 'account/staff/staff-form.html', context)
        else:
            raise Http404()


@staff_only
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

#         return render(request, 'account/staff/register-staff.html', context)
