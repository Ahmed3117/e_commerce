
from .models import Category

def navinfo(request):
    categories = Category.objects.all()
    user_waiting_cart_items=0
    user_pilled_cart_items=0
    user_loved_items =0
    if request.user.username != '':
        user_waiting_cart_items=request.user.cartitem_set.filter(user=request.user,status = 'waiting').count()
        user_pilled_cart_items=request.user.cartitem_set.filter(user=request.user,status = 'pilled').count()
        user_loved_items=request.user.love_set.all().count()
    ##################################################
    # paths history
    context = {
        'categories' : categories, 
        'user_waiting_cart_items' : user_waiting_cart_items, 
        'user_pilled_cart_items' : user_pilled_cart_items, 
        'user_loved_items' : user_loved_items, 
    }
    return (context)

