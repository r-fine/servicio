from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.text import slugify

from django_tables2 import SingleTableView, MultiTableMixin

from apps.accounts.models import LocalUser, Staff
from apps.accounts.tables import StaffTable, CategoryTable, ServiceTable, OrderTable
from apps.accounts.decorators import admin_required, admin_only
from apps.services.forms import CategoryCreationForm, ServiceCreationForm
from apps.services.models import Category, Service
from apps.orders.models import Order
from apps.orders.forms import AdminOrderForm

# class AdminRequiredMixin(UserPassesTestMixin):
#     def test_func(self):
#         return self.request.user.is_superuser


@admin_required()
class StaffTableView(SingleTableView):
    model = Staff
    table_class = StaffTable
    template_name = "account/admin/staff-list.html"
    # table_data = Staff.objects.all()
    # paginator_class = LazyPaginator


def dashboard_admin(request):

    return render(request, 'account/admin/admin-dashboard.html')


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


# @admin_required()
class CategoryServiceTableView(MultiTableMixin, TemplateView):
    template_name = "account/admin/category-service-list.html"
    tables = [
        CategoryTable(Category.objects.all()),
        ServiceTable(Service.objects.all())
    ]
    table_pagination = {
        "per_page": 25
    }


@admin_required()
class CategoryCreateView(SuccessMessageMixin, CreateView):
    template_name = 'account/admin/create-category.html'
    form_class = CategoryCreationForm
    success_url = reverse_lazy('accounts:create_category')
    success_message = "A new category has been added"

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_name"] = "Add new Category"
        return context


@admin_only
def edit_category(request, category_id):
    category = Category.objects.get(pk=category_id)

    if request.method == 'POST':
        form = CategoryCreationForm(
            request.POST, request.FILES, instance=category)
        if form.is_valid():
            category.save()
            return redirect('accounts:category_table')
        else:
            return HttpResponse('failed to submit')
    else:
        form = CategoryCreationForm(instance=category)
        context = {
            'form': form,
            'form_name': 'Edit Category'
        }

        return render(request, 'account/admin/create-category.html', context)


@admin_only
def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()

    return redirect('accounts:product_table')


@admin_required()
class ServiceCreateView(SuccessMessageMixin, CreateView):
    template_name = 'account/admin/create-service.html'
    form_class = ServiceCreationForm
    success_url = reverse_lazy('accounts:create_service')
    success_message = "A new service has been added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_name"] = "Add new Service"
        return context


@admin_only
def edit_service(request, service_id):
    service = Service.objects.get(pk=service_id)

    if request.method == 'POST':
        form = ServiceCreationForm(
            request.POST, request.FILES, instance=service)
        if form.is_valid():
            service.save()
            return redirect('accounts:service_table')
        else:
            return HttpResponse('failed to submit')
    else:
        form = ServiceCreationForm(instance=service)
        context = {
            'form': form,
            'form_name': 'Edit Sevice'
        }

        return render(request, 'account/admin/create-service.html', context)


@admin_only
def delete_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    service.delete()

    return redirect('accounts:product_table')


@admin_required()
class OrderTableView(SingleTableView):
    model = Order
    table_class = OrderTable
    template_name = 'account/admin/order-list.html'


# @admin_only
# def edit_order(request, order_id):
#     pass


@admin_only
def order_set_cancel(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.status = 'Completed'
    order.is_ordered = True
    order.save()

    return HttpResponse('success!')


@admin_required()
class OrderUpdateForm(SuccessMessageMixin, UpdateView):
    model = Order
    form_class = AdminOrderForm
    template_name = "account/admin/order-edit.html"
    success_url = reverse_lazy('accounts:order_table')
    success_message = 'Order has been updated.'

    def form_valid(self, form):
        if form.instance.status == 'Completed':
            form.instance.is_ordered = True

        return super().form_valid(form)
