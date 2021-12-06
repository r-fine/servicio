from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.safestring import mark_safe

from allauth.account.decorators import verified_email_required

from apps.orders.models import Order, OrderItem


def user_dashboard(request):
    return render(request, 'account/user-dashboard.html')


@verified_email_required
def order_history(request):
    user = request.user
    active = Order.objects.filter(
        user=user, status__in=('New', 'Accepted', 'OTW')
    )
    completed = Order.objects.filter(user=user, status='Completed')
    cancelled = Order.objects.filter(user=user, status='Cancelled')

    context = {
        'active': active,
        'completed': completed,
        'cancelled': cancelled,
    }
    return render(request, 'order/order-history.html', context)


def cancel_order(request, order_id):
    order = Order.objects.get(user=request.user, id=order_id)
    if order.status == 'OTW':
        messages.error(request, mark_safe(
            'The order you are requesting to cancel is already on the way. Please <a href="mailto:info@example.com">contact us<a> to cancel your order.'))
    else:
        order.status = 'Cancelled'
    order.save()

    return redirect('accounts:order_history')
