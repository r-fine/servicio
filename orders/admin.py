from django.contrib import admin

from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['area', 'order_number', 'created_at', 'updated_at']


admin.site.register(OrderProduct)
