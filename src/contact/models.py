from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank = True)
    mail = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100, null=True, blank = True)
    message = models.TextField(max_length=1000, null=True, blank = True)