import random
import os
import string
from django.contrib.auth.models import User
from django.db import models


import products
# from django.utils import timezone
# Create your models here.

    
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    def __str__(self):
        return self.category.name + ' ' +self.name
class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/', null = True , blank = True)
    def __str__(self):
        return self.name
    
class Image(models.Model):
    image = models.ImageField(upload_to='products/', null = True , blank = True)
    def __str__(self):
        return os.path.basename(self.image.name)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ManyToManyField(Image)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, null = True , blank = True)
    sub_category = models.ForeignKey(SubCategory , on_delete=models.CASCADE, null = True , blank = True)
    brand = models.ForeignKey(Brand , on_delete=models.CASCADE, null = True , blank = True)
    price = models.FloatField(null = True , blank = True)
    description = models.TextField(max_length=1000, null = True , blank = True)
    date_added = models.DateTimeField(auto_now=True, auto_now_add=False)
    num_of_sales = models.IntegerField(default = 0)
    rate = models.FloatField(default = 0.0)
    def priceafterproductdiscount(self):
        last_product_discount = self.discount_set.last()
        price_after_product_discount = 0
        if last_product_discount:
            price_after_product_discount = self.price - ((last_product_discount.discount / 100) * self.price)
        else:
            price_after_product_discount = self.price
        return price_after_product_discount
    def priceaftercategorydiscount(self):
        last_category_discount = self.category.discount_set.last()
        price_after_category_discount = 0
        if last_category_discount:
            price_after_category_discount = self.price - ((last_category_discount.discount / 100) * self.price)
        else:
            price_after_category_discount = self.price
        return price_after_category_discount
    def discountstatus(self):
        discount_status = False
        if self.priceafterproductdiscount != self.price:
            discount_status = True
        return discount_status
    def mainimage(self):
        images = self.image.all()
        main_image = images[0]
        if len(images)>0 :
            main_image = random.choice(images)
        return main_image
    def images(self):
        images = self.image.all()
        return images
    def get_number_of_ratings(self): # number of reviews
        ratings = self.rating_set.all()
        number_of_ratings = ratings.count()
        return number_of_ratings
    def get_product_rate(self):
        ratings = self.rating_set.all()
        rate = 0.0
        rating_list = []
        for rating in ratings:
            rating_list.append(rating.star_number)
        if len(rating_list) > 0 :
            rate = round(sum(rating_list)/len(rating_list),1)
        return rate
    def get_product_quantity(self):
        product_availability= self.productavailability_set.all()
        quantity = 0
        for product in product_availability :
            quantity += product.quantity
        return quantity
    def get_product_colors(self):
        product_availability= self.productavailability_set.all()
        colors=[]
        for product in product_availability :
            colors.append(product.color.name)
        return colors
    def get_product_sizes(self):
        product_availability= self.productavailability_set.all()
        sizes=[]
        for product in product_availability :
            sizes.append(product.size)
        return sizes
    def __str__(self):
        return self.name
################################
sizes_choices=[
    ('s','s'),
    ('xs','xs'),
    ('m','m'),
    ('l','l'),
    ('xl','xl'),
    ('xxl','xxl'),
    ('xxxl','xxxl'),
]
class Color(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class ProductAvailability(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE, null = True , blank = True)
    size = models.CharField(choices=sizes_choices ,max_length=50,default='s')
    color = models.ForeignKey(Color , on_delete=models.CASCADE, null = True , blank = True)
    quantity = models.IntegerField(null = True , blank = True)
    def __str__(self):
        return self.product.name + '-' + self.size + '-' + self.color.name + '-' + str(self.quantity)
class Rating(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, null = True , blank = True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE, null = True , blank = True)
    star_number = models.FloatField(default = 5.0)
    review =models.CharField(max_length=300, default = "no review comment")
    date_added = models.DateField(auto_now=True)
    # 'star_range' :range(0,int(str(product.get_product_rate())[0])),
    # 'empty_star_range_if_no_half_star' :range(0,5-int(str(product.get_product_rate())[0])),
    def star_ranges(self):
        star_number_range = range(0,int(self.star_number))
        empty_star_range = range(0,5-int(self.star_number))
        return star_number_range,empty_star_range
    def __str__(self):
        return self.product.name + " " + self.user.username

pill_status_choices=[
    ('delivered','delivered'),
    ('underdeliver','underdeliver'), # if underdeliver , cartitems will be removed and the pill will be waiting for being delivered
    ('waiting','waiting'),
]
cartitem_status_choices=[
    ('done','done'),
    ('waiting','waiting'),
    ('pilled','pilled'),
]
class CartItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, null = True , blank = True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE, null = True , blank = True)
    quantity = models.IntegerField(null = True , blank = True)
    size = models.CharField(choices=sizes_choices ,max_length=50,default='s')
    color = models.ForeignKey(Color , on_delete=models.CASCADE, null = True , blank = True)
    status = models.CharField(choices=cartitem_status_choices ,max_length=50,default='waiting')
    def get_cart_item_price(self): # total
        if self.product.priceafterproductdiscount()<self.product.price:
            cart_item_price = self.product.priceafterproductdiscount() * self.quantity
        else:
            cart_item_price = self.product.priceaftercategorydiscount() * self.quantity
        return cart_item_price
    def get_cart_item_single_price(self):
        return self.get_cart_item_price() / self.quantity

class Shipping(models.Model):
    shipping_price=models.FloatField(default=0.0)
    
class Pill(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, null = True , blank = True)
    cartitem = models.ManyToManyField(CartItem, null = True , blank = True)
    pill_discount = models.FloatField(default = 0.0)
    pill_coupon_discount = models.FloatField(default = 0.0)
    status = models.CharField(choices=pill_status_choices ,max_length=50,default='waiting')
    date_added = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default = False)
    def get_pill_price(self):
        pill_items = self.cartitem.all()
        pill_price = 0.0
        for item in pill_items:
            pill_price += item.get_cart_item_price()
        pill_price_afterdiscount =pill_price - (self.pill_discount / 100) * pill_price
        shipping_price = Shipping.objects.last().shipping_price
        pill_price_afterdiscount_and_shipping =pill_price - (self.pill_discount / 100) * pill_price + shipping_price
        pill_price_afterdiscount_and_shipping_and_coupon =pill_price - (self.pill_discount / 100) * pill_price - (self.pill_coupon_discount / 100) * pill_price + shipping_price
        
        return pill_price , pill_price_afterdiscount , pill_price_afterdiscount_and_shipping , pill_price_afterdiscount_and_shipping_and_coupon , shipping_price
class Love(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, null = True , blank = True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE, null = True , blank = True)
    
class Discount(models.Model):
    discount = models.FloatField(null = True , blank = True)
    discount_start = models.DateTimeField()
    discount_end = models.DateTimeField()
    comment = models.CharField(max_length=150 , null = True , blank = True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, null = True , blank = True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE, null = True , blank = True)
    
class CouponDiscount(models.Model):
    coupon = models.CharField(
        max_length = 100,
        blank=True,
        null=True,
        editable=False)
    discount_value = models.FloatField(null = True , blank = True)
    coupon_start = models.DateTimeField(null = True , blank = True)
    coupon_end = models.DateTimeField(null = True , blank = True)
    def save(self, *args, **kwargs):
        self.coupon = create_random_coupon()
        super().save(*args, **kwargs)

def create_random_coupon():
    letters = string.ascii_lowercase # small letters
    nums = ['0','2','3','4','5','6','7','8','9']
    marks = ['@','#','$','%','&','*']
    return '-'.join(random.choice(letters)+random.choice(nums)+random.choice(marks) for i in range(5))