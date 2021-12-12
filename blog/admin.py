from django.contrib import admin
from .models import Package, OrderDetail


admin.site.register(Package)
admin.site.register(OrderDetail)
