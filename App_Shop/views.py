from django.shortcuts import render
from App_Shop.models import Product

# Create your views here.


def Home(request):
    new_product = Product.objects.new_items()
    top_product = Product.objects.top_items()
    top1 = top_product[0:3]
    top2 = top_product[3:6]
    top3 = top_product[6:9]
    top4 = top_product[9:12]
    context = {
        'new_product': new_product,
        'top_product': top_product,
        'top1': top1,
        'top2': top2,
        'top3': top3,
        'top4': top4
    }
    return render(request, 'App_Shop/home.html', context)