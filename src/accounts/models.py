
from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=50, null=True, blank = True)
    
class UserAdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True,upload_to='userimages/' ,default="/static/img/avatar.jpeg")
    def __str__(self):
        return self.user.username

######################################################
# using modifying the User model
