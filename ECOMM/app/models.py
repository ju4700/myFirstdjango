from django.contrib.auth.models import User
from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('D', 'DELL'),
    ('H', 'Hp'),
    ('As', 'Asus'),
    ('Ac', 'Acer'),
    ('M', 'MSI'),
    ('L', 'Lenovo'),
)
STATE_CHOICES = (
    ('Dhaka', 'Dhaka'),
    ('Chittagong', 'Chittagong'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur'),
    ('Sylhet', 'Sylhet'),
    ('Barisal', 'Barisal'),
    ('Khulna', 'Khulna'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    mobile = models.IntegerField()
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATE_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
    ('Pending', 'Pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Cancelled', 'Cancelled')], default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
