from django.contrib import admin
from .models import Product, Category, Cart, Order, OrderItem


admin.site.register([Product, Category, Cart, Order, OrderItem])
