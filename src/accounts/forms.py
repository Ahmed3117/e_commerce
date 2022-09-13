from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# form for register
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']

# form for update user
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']
