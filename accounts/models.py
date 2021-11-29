from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

from services.models import Category


class LocalUser(AbstractUser):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(verbose_name='E-mail Address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        if self.is_superuser:
            return self.username
        return self.get_full_name


class Staff(models.Model):
    department = models.ForeignKey(
        Category,
        related_name='department',
        null=True,
        on_delete=models.SET_NULL
    )
    user = models.OneToOneField(LocalUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        verbose_name='Profile Picture',
        upload_to='images/profile_pic/',
    )
    phone = models.CharField(verbose_name='Phone Number', max_length=11)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(
        verbose_name='Active status', default=False
    )

    @property
    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name

    def get_user_id(self):
        return self.user.id

    def get_absolute_url(self):
        return reverse('accounts:staff_form', args=[self.pk])

    def delete_staff(self):
        return reverse('accounts:staff_delete', args=[self.pk])

    def activate_user(self):
        return reverse('accounts:staff_activate', args=[self.pk])

    def __str__(self):
        return self.get_full_name
