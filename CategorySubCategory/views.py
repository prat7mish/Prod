from django.shortcuts import render,HttpResponse
from django.http import HttpResponse, HttpResponseNotFound
from .models import Product,Category,SubCategory
# Create your views here.
def index(request):
    product=Product.objects.all()
    context={'product':product}
    return render(request,'CategorySubCategory/index.html',context) 


def addProduct(request):
    print(request.POST)
    cat=request.POST.get('category')
    subcat=request.POST.get('subcategory')
    prod=request.POST.get('product')
    if request.method=="POST":
        c=Category.objects.get(name=cat)
        s=SubCategory.objects.get(name=subcat)
        Product.objects.create(name=prod,category=c,subcategory=s)
    else:
        print("get")
    return HttpResponse("/")