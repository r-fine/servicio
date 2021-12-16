from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.safestring import mark_safe
from django.core.paginator import Paginator

from allauth.account.decorators import verified_email_required

from apps.orders.models import Order, OrderItem
# from apps.accounts.decorators import allowed_users


def user_dashboard(request):
    return HttpResponse('User Dashboard')
    # return render(request, 'account/user-dashboard.html')


@verified_email_required
def order_history(request):
    order_list = Order.objects.prefetch_related('order_item').filter(
        user=request.user).order_by('-created_at')

    page_obj = request.GET.get('page', 1)

    paginator = Paginator(order_list, 3)

    try:
        orders = paginator.page(page_obj)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {
        'orders': orders,
    }
    return render(request, 'order/order-history.html', context)


def cancel_order(request, op_id):
    op = OrderItem.objects.get(user=request.user, id=op_id)
    if op.status == 'Preparing':
        messages.error(request, mark_safe(
            'This order is already on progress. Please <a href="mailto:info@example.com">contact us<a> to cancel your order.'))
    else:
        op.status = 'Cancelled'
    op.save()

    return redirect('accounts:order_history')
