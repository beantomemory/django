from django.shortcuts import render
from .models import *

# Create your views here.
def Upimg(request):
    if request.method == "POST":
        new_brand = Brand()
        new_brand.logo = request.FILES.get("picc")
        new_brand.title = "BWM"
        new_brand.newprice = 11.11
        new_brand.save()
    if request.method == "GET":
        return render(request, "upimg.html")