from django.shortcuts import render

# Create your views here.
def shop_view(request,*args,**kwargs):
    return render(request,"comingsoon.html")



