from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=100, null=True, blank = True)
    logo = models.ImageField(upload_to='Logo/', height_field=None, width_field=None, max_length=None, null=True, blank = True)
    description = models.TextField(max_length=1000, null=True, blank = True)
    phone = models.CharField(max_length=20, null=True, blank = True)
    mail = models.EmailField(max_length=254, null=True, blank = True)
    address = models.CharField(max_length=200, null=True, blank = True)
    class Meta:
        verbose_name_plural = 'Shop information'
    def __str__(self):
        return self.name

# wait for a while
class Coupon(models.Model):
    coupon = models.CharField(max_length=100)

