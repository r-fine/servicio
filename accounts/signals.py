from django.dispatch import receiver
from django.contrib.auth.models import Group

from allauth.account.signals import user_logged_in

from .models import Staff


@receiver(user_logged_in)
def staff_profile(request, user, **kwargs):
    if user.is_superuser == False and user.is_staff:
        if not Staff.objects.filter(user=user).exists():
            group = Group.objects.get(name='STAFF')
            group.user_set.add(user)
            Staff.objects.create(user=user)
            print(
                '#########################  P R O F I L E  C R E A T E D  #########################')
