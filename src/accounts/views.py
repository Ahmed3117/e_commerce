from django.shortcuts import redirect, render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

from accounts.models import UserAdditionalInfo
# from .models import Room, Topic, Message, User
from .forms import UserForm, MyUserCreationForm
# Create your views here.

def loginUser(request):
    page = 'login'
    # if request.user.is_authenticated:
    #     return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'accounts/login-register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')


def registerUser(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # create object in the UserAdditionalInfo model 
            user_more_info = UserAdditionalInfo.objects.create(user=user)
            user_more_info.save()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'accounts/login-register.html', {'form': form})


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    user_additional_information, created = UserAdditionalInfo.objects.get_or_create(user = user)
    # user_additional_information = UserAdditionalInfo.objects.get(user = user) 
    im = user_additional_information.image.url
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        user.username = username
        user.email = email
        user_additional_information.image = image
        user_additional_information.save()
        user.save()
        # user.useradditionalinfo.save()
        return redirect('/')

    return render(request, 'accounts/update-user.html', {'user': user,'im': im})



################################################################3
# updateUser using forms:

# @login_required(login_url='login')
# def updateUser(request):
#     user = request.user
#     form = UserForm(instance=user)

#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     return render(request, 'accounts/update-user.html', {'form': form})