from django.shortcuts import render

# Create your views here.
def preloader_view(request,*args,**kwargs):
    return render(request,'preloader.html')