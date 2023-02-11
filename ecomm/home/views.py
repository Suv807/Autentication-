from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    #populating products in home page
    context={'products': Product.objects.all()}
    return render(request, 'home/index.html',context)