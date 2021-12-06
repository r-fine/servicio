from django.contrib import admin

from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'id', 'area', 'created_at',
                    'updated_at', 'user_verification_status']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['service', 'user', 'order', 'is_active']
