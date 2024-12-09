from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ECOMM import settings
from .models import Product, Customer, Cart, Payment, OrderPlaced
from .froms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from uuid import uuid4
import requests
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        tite = Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html', locals())

class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        tite = Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'app/category.html', locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, "app/productdetail.html", locals())

class CustomerRgistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer registration was successful')
        else:
            messages.warning(request, 'Something went wrong')
        return render(request, 'app/customerregistration.html', locals())

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Profile was successful')
        else:
            messages.warning(request, 'Something went wrong')
        return render(request, 'app/profile.html', locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', locals())

class updateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'app/updateAddress.html', locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, 'Address was successful')
        else:
            messages.warning(request, 'Something went wrong')
        return redirect("address")

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect("/cart")

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 1200
    return render(request, 'app/addtocart.html', locals())

class checkout(View):
    def get(self, request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 1200
        return render(request, 'app/checkout.html', locals())

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        try:
            cart_items = Cart.objects.filter(Q(product=prod_id) & Q(user=request.user))
            if not cart_items.exists():
                return JsonResponse({'error': 'Cart item not found.'}, status=404)
            c = cart_items.first()
            c.quantity += 1
            c.save()
            user = request.user
            cart = Cart.objects.filter(user=user)
            amount = sum(item.quantity * item.product.discounted_price for item in cart)
            totalamount = amount + 1200
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': totalamount,
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        try:
            cart_items = Cart.objects.filter(Q(product=prod_id) & Q(user=request.user))
            if not cart_items.exists():
                return JsonResponse({'error': 'Cart item not found.'}, status=404)
            c = cart_items.first()
            c.quantity -= 1
            c.save()
            user = request.user
            cart = Cart.objects.filter(user=user)
            amount = sum(item.quantity * item.product.discounted_price for item in cart)
            totalamount = amount + 1200
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': totalamount,
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')
        try:
            cart_items = Cart.objects.filter(Q(product=prod_id) & Q(user=request.user))
            if not cart_items.exists():
                return JsonResponse({'error': 'Cart item not found.'}, status=404)
            cart_items.delete()
            user = request.user
            cart = Cart.objects.filter(user=user)
            amount = sum(item.quantity * item.product.discounted_price for item in cart)
            totalamount = amount + 1200  # Assuming 1200 is the shipping cost or fixed fee
            data = {
                'amount': amount,
                'totalamount': totalamount,
            }
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@login_required
def payment_view(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to proceed with payment.')
        return redirect('login')

    user = request.user
    cart_items = Cart.objects.filter(user=user)

    if not cart_items.exists():
        messages.warning(request, 'Your cart is empty. Please add items to the cart.')
        return redirect('index')

    amount = sum(item.quantity * item.product.discounted_price for item in cart_items)
    total_amount = amount + 1200

    customer = Customer.objects.filter(user=user).first()
    if not customer:
        messages.warning(request, 'Please update your profile before proceeding with payment.')
        return redirect('profile')

    transaction_id = uuid4().hex

    data = {
        'store_id': settings.SSL_COMMERZ['store_id'],
        'store_passwd': settings.SSL_COMMERZ['store_passwd'],
        'total_amount': str(total_amount),
        'currency': 'BDT',
        'tran_id': transaction_id,
        'success_url': request.build_absolute_uri('/payment-success/?tran_id=' + transaction_id),
        'fail_url': request.build_absolute_uri('/payment-fail/'),
        'cancel_url': request.build_absolute_uri('/payment-cancel/'),
        'cus_name': customer.name,
        'cus_email': user.email,
        'cus_phone': customer.mobile,
        'cus_add1': customer.locality,
        'cus_add2': customer.city,
        'product_name': 'Cart Items',
        'product_category': 'Products',
        'product_profile': 'general',
    }

    url = 'https://sandbox.sslcommerz.com/gwprocess/v3/api.php'  # Use sandbox for testing
    response = requests.post(url, data=data)
    response_data = response.json()

    if response_data.get('status') == 'SUCCESS':
        return redirect(response_data['GatewayPageURL'])
    else:
        messages.error(request, 'Payment initiation failed. Please try again.')
        return redirect('checkout')

@csrf_exempt
@login_required
def payment_success(request):
    transaction_id = request.GET.get('tran_id')

    order = OrderPlaced.objects.filter(transaction_id=transaction_id).first()

    if order:
        order.payment_status = 'Success'
        order.save()
        messages.success(request, 'Payment Successful! Your course has been added to your account.')

        context = {
            'transaction_id': transaction_id,
            'amount': order.total_amount,
        }
    else:
        messages.error(request, 'Transaction not found or payment failed.')
        context = {}

    return render(request, 'app/payment_success.html', context)

@csrf_exempt
@login_required
def payment_fail(request):
    messages.error(request, 'Payment Failed. Please try again or contact support.')
    return redirect('cart')