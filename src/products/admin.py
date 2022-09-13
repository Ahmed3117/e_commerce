from django.contrib import admin

from .models import Color,Shipping,ProductAvailability,Brand, CartItem,Pill,CouponDiscount ,Category, Discount,Image,Love,Product,Rating,SubCategory
# Register your models here.
admin.site.register(ProductAvailability)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(CartItem)
admin.site.register(Pill)
admin.site.register(CouponDiscount)
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Image)
admin.site.register(Love)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(SubCategory)
admin.site.register(Shipping)

