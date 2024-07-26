from django.shortcuts import render

def index(request):
    return render(request, 'menu/index.html')

def shop_top(request):
    return render(request, 'menu/shop/clothing/top.html')



