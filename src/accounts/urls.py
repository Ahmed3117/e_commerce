from django.urls import path
from . import views 
app_name = 'accounts'
urlpatterns = [
    # path('login/',views.login,name = 'login'),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('update-user/', views.updateUser, name="update-user"),
    
]