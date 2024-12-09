from django.contrib import admin
from .models import Product, Customer, Cart, Payment, OrderPlaced


# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'paid']
    search_fields = ['user__username']
    list_filter = ['paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'order_date', 'status', 'payment']
    search_fields = ['user__username', 'customer__name', 'product__title']
    list_filter = ['status', 'order_date']
    date_hierarchy = 'order_date'
    list_select_related = ['user', 'customer', 'product', 'payment']