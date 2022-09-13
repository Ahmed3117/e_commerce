from email import message
import json
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from .models import Brand, CartItem, Category, Color, CouponDiscount, Discount,Image,Love, Pill,Product, Rating, Shipping,SubCategory
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.


##############################################################
def get_product_rate():
    products = allproducts()
    for product in products :
        rate = 0.0
        rating_list = []
        ratings = product.rating_set.all()
        for rating in ratings:
            rating_list.append(rating.star_number)
        if len(rating_list) > 0 :
            rate = round(sum(rating_list)/len(rating_list),1)
            print(rate)
        product.rate = rate
        product.save()
    print('executed ==============================')
#############################################################
def allproducts():
    products = Product.objects.all()
    return products
def popularproducts():
    products = allproducts().order_by('-num_of_sales')
    return products
def latestproducts():
    products = allproducts().order_by('-date_added')
    return products
def bestratedproducts():
    products = allproducts().order_by('-rate')
    return products
def filteredproducts(request):
    search = request.GET.get('search') or ''
    category = request.GET.get('category') or ''
    sub_category = request.GET.get('sub_category') or ''
    brand = request.GET.get('brand') or ''
    sort = request.GET.get('sort') or ''
    
    products = allproducts()
    if category :
        if sub_category :
            products = products.filter(category__name=category,sub_category__name=sub_category)
        else :
            products = products.filter(category__name=category)
    elif brand :
        products = products.filter(brand__name=brand)
    elif search :
        products = products.filter(name__icontains=search)
    elif sort :
        if sort == 'latest':
            products = latestproducts()
        elif sort == 'popular' : # most saled 
            products = popularproducts()
        elif sort == 'best_rated' :
            get_product_rate()
            products = bestratedproducts()

    return products
def paginate(request):
    paginator = Paginator(filteredproducts(request), 6)
    page = request.GET.get('page')
    return paginator.get_page(page)
def shop(request):
    products = paginate(request)
    all_products_number=allproducts().count()
    filter_0_10=allproducts().filter(price__gte=0,price__lte=10)
    filter_0_10_number = filter_0_10.count()
    filter_10_20=allproducts().filter(price__gte=10,price__lte=20)
    filter_10_20_number = filter_10_20.count()
    filter_20_30=allproducts().filter(price__gte=20,price__lte=30)
    filter_20_30_number = filter_20_30.count()
    filter_30_40=allproducts().filter(price__gte=30,price__lte=40)
    filter_30_40_number=filter_30_40.count()
    filter_40_50=allproducts().filter(price__gte=40,price__lte=50)
    filter_30_40_number=filter_30_40.count()
    context = {
        'products' : products, 
        'all_products_number' : all_products_number, 
        'filter_0_10_number' : filter_0_10_number, 
        'filter_10_20_number' : filter_10_20_number, 
        'filter_20_30_number' : filter_20_30_number, 
        'filter_30_40_number' : filter_30_40_number, 
        'filter_30_40_number' : filter_30_40_number, 
        
    }
    return render(request,'products/shop.html',context)

def pricefilter(request):
    filter_20_30=allproducts().filter(price__gte=20,price__lte=30)
    filter_20_30_number = filter_20_30.count()
    filter_30_40=allproducts().filter(price__gte=30,price__lte=40)
    filter_30_40_number=filter_30_40.count()
    filter_40_50=allproducts().filter(price__gte=40,price__lte=50)
    filter_30_40_number=filter_30_40.count()
##############################################################
def home(request):
    popular_products = popularproducts()[:6]
    latest_products = latestproducts()[:6]
    now= timezone.now()
    offers = Discount.objects.filter(discount_end__gte = now , discount_start__lte = now)
    category_offers = offers.filter(product__isnull=True)
    product_offers = offers.filter(product__isnull=False)
    
    context = {
        'popular_products' : popular_products, 
        'latest_products' : latest_products, 
        'offers' : offers, 
        'category_offers' : category_offers, 
        'product_offers' : product_offers, 
    }
    return render(request,'products/home.html',context)

###############################################################
def productdetail(request,product_id):
    product = Product.objects.get(id = product_id)
    related_products = Product.objects.filter(category = product.category)
    ratings = product.rating_set.all()
    paginator = Paginator(ratings, 4)
    page = request.GET.get('page')
    ratings = paginator.get_page(page)

    context = {
        'product' : product,
        'related_products' : related_products,
        'product_rate' :product.get_product_rate(),
        'product_rate_int_part' :int(str(product.get_product_rate())[0]),
        'product_rate_float_part' :int(str(product.get_product_rate())[-1]),
        'star_range' :range(0,int(str(product.get_product_rate())[0])),
        'empty_star_range_if_no_half_star' :range(0,5-int(str(product.get_product_rate())[0])),
        'empty_star_range_if_there_is_half_star' :range(0,4-int(str(product.get_product_rate())[0])),
        'ratings' : ratings,
    }
    return render(request,'products/detail.html',context)

def review(request,product_id):
    star_number = 0.0
    user = request.user
    product = Product.objects.get(id = product_id)
    review = request.POST.get('review')
    star1 = request.POST.get('star1')
    star2 = request.POST.get('star2')
    star3 = request.POST.get('star3')
    star4 = request.POST.get('star4')
    star5 = request.POST.get('star5')
    if star1 == "on" :
        star_number += 1.0
    if star2 == "on" :
        star_number += 1.0
    if star3 == "on" :
        star_number += 1.0
    if star4 == "on" :
        star_number += 1.0
    if star5 == "on" :
        star_number += 1.0
    user_review = Rating.objects.update_or_create(user=user,product=product,star_number=star_number,review=review)
    # user_review.save()
    return redirect('products:detail' ,product.id )

def addtocard(request,product_id):
    user = request.user
    product = Product.objects.get(id = product_id)
    size = request.POST.get('size') or ''
    color = request.POST.get('color') or ''
    color_obj = Color.objects.get(name=color)
    quantity = request.POST.get('quantity') or ''
    if size and color:
        added_item = CartItem.objects.create(user=user,product=product,size=size,color=color_obj,quantity=quantity)
        added_item.save()
        messages.info(request, 'added successfully to your cart')
        return redirect('products:detail' ,product.id )
    else:
        messages.error(request, 'some data is lost')
        return redirect('products:detail' ,product.id )

def mycartcontent(request):
    user = request.user
    cartitems = []
    if request.user.username != '':
        cartitems = CartItem.objects.filter(user = user).exclude(status = 'done')
    total_price = 0.0
    for item in cartitems:
        total_price += item.get_cart_item_price()
    # pills = []
    # if request.user.username != '':
    #     pills = Pill.objects.filter(user = user,status = 'waiting')
    context = {
        'cartitems' : cartitems,
        'total_price' : total_price,
    }
    return render(request,'products/cart.html',context)

def updatecartitem(request,cartitem_id):
    quantity = request.POST.get('quantity'+ cartitem_id) or ''
    cartitem = CartItem.objects.get(id = cartitem_id)
    if quantity:
        cartitem.quantity = quantity
        cartitem.save()
    return redirect('products:cart')
def deletecartitem(request, cartitem_id):
    cartitem = get_object_or_404(CartItem, id=cartitem_id)
    cartitem.delete()
    return redirect('products:cart')

def createorupdatepill(request):
    user = request.user
    cartitems = CartItem.objects.filter(user = user , status = 'waiting')
    pill, created = Pill.objects.update_or_create(
        user=user,status = "waiting"
    )
    for item in cartitems:
        pill.cartitem.add(item)
        item.status = 'pilled'
        item.save()
    return redirect('products:mypill')

def mypill(request):
    user = request.user
    coupon = ''
    coupon_status = None
    now= timezone.now()
    try:
        pill = Pill.objects.get(user = user,status = 'waiting')
        shipping = Shipping.objects.last().shipping_price
        user_entered_coupon = request.GET.get('coupon') or ''
        try:
            coupon = CouponDiscount.objects.get(coupon_end__gte = now , coupon_start__lte = now,coupon = user_entered_coupon)
            if pill.pill_coupon_discount == 0 :
                pill.pill_coupon_discount = coupon.discount_value
                pill.save()
            else:
                coupon_status = 'active'
        except:
            coupon = None
    except:
        pill = None
        shipping = 0.0
    context = {
        'pill' : pill,
        'shipping' : shipping,
        'coupon' : coupon,
        'coupon_status' : coupon_status,
    }
    return render(request,'products/checkout.html',context)

def pillpaid(request): # to update pill pay status to be paid after paying process
    body = json.loads(request.body)
    pill = Pill.objects.get(id=body['pill_id'])
    pill.paid = True
    pill.status = "underdeliver"
    pill.save()
    pill_items = pill.cartitem.all()
    for item in pill_items:
        item.status = "done"
        item.save()
    return JsonResponse("payment complted")
    


