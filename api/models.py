from django.db import models
from django.contrib.auth.models import User 
from cloudinary.models import CloudinaryField

# image = models.ImageField(upload_to='products/', null=False, blank=False)

class Shop(models.Model):
    name = models.CharField(max_length=255)
    shop_id = models.AutoField(primary_key=True)
    
    def __str__(self):
            return self.name

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('phones', 'Phones'),
        ('speakers', 'Speakers'),
        ('laptops', 'Laptops'),
        ('footwears', 'Footwears'),
        ('appliances', 'Appliances'),
        ('clothing', 'Clothings'),

    ]


    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="appliances")
    image = CloudinaryField('image', folder='shopping', null=False, blank=False)
    # image = models.ImageField(upload_to="products/",null=True, blank=True)
    product_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f"{self.name}"
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Each user has one cart

    def __str__(self):
        return f"Cart - {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
