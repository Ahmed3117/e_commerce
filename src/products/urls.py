from django.urls import path
from . import views 
app_name = 'products'
urlpatterns = [
    path('',views.home,name = 'home'),
    path('shop/',views.shop,name = 'shop'),
    path('shop/<str:product_id>',views.productdetail,name = 'detail'),
    path('shop/<str:product_id>/review/',views.review,name = 'review'),
    path('shop/<str:product_id>/addtocart/',views.addtocard,name = 'addtocard'),
    path('cart/<str:cartitem_id>/updatecart/',views.updatecartitem,name = 'updatecart'),
    path('cart/<str:cartitem_id>/deletecartitem/',views.deletecartitem,name = 'deletecartitem'),
    path('createorupdatepill/',views.createorupdatepill,name = 'createorupdatepill'),
    path('mypill/',views.mypill,name = 'mypill'),
    path('pillpaid',views.pillpaid,name = 'pillpaid'),
    path('cart/',views.mycartcontent,name = 'cart'),
]