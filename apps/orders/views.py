from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from allauth.account.decorators import verified_email_required

from apps.services.models import Service
from .models import Order, OrderItem
from .forms import OrderForm

import datetime


class OrderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "order/order-form.html"
    form_class = OrderForm
    success_url = reverse_lazy('accounts:order_history')
    success_message = 'Order placed successfully'

    def form_valid(self, form):
        year = int(datetime.date.today().strftime('%Y'))
        month = int(datetime.date.today().strftime('%m'))
        date = int(datetime.date.today().strftime('%d'))
        s = int(datetime.datetime.now().strftime('%S'))
        if len(str(s)) == 1:
            s = '6'+str(s)
        else:
            s = str(s)
        order_date = datetime.date(year, month, date)
        current_date = order_date.strftime("%Y%m%d")
        order_number = current_date + str(form.instance.phone[7:]) + s

        form.instance.user = self.request.user
        form.instance.order_number = order_number

        order_items = OrderItem.objects.filter(
            user=self.request.user, is_active=True
        )

        self.object = form.save()

        for item in order_items:
            item.is_active = False
            item.order = form.instance
            item.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = OrderItem.objects.filter(
            user=self.request.user, is_active=True
        )

        return context


@login_required
def add_order(request, service_id):

    service = Service.objects.get(id=service_id)

    try:
        order_item = OrderItem.objects.get(
            user=request.user,
            service=service,
            is_active=True
        )
        messages.warning(request, 'Already added to order list.')

    except OrderItem.DoesNotExist:
        order_item = OrderItem.objects.create(
            user=request.user,
            service=service,
            is_active=True
        )
        order_item.save()
        messages.success(request, 'Added to order list.')

    return redirect('orders:order_create')


@login_required
def remove_item(request, service_id, order_item_id):

    service = Service.objects.get(id=service_id)
    order_item = OrderItem.objects.get(
        service=service,
        user=request.user,
        id=order_item_id
    )
    order_item.delete()
    messages.error(request, 'Removed from order')

    return redirect('orders:order_create')
