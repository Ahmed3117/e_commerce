
from .models import About

def shopinfo(request):
    shop_info = About.objects.last()
    context = {
        "shop_info" : shop_info,
    }
    return (context)