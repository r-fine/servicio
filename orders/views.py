from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from allauth.account.decorators import verified_email_required

from .models import Order
from .forms import OrderForm

import datetime


class OrderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "order/order-form.html"
    form_class = OrderForm
    success_url = reverse_lazy('services:home')
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

        return super().form_valid(form)
