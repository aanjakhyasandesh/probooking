from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def shop_view(request,*args,**kwargs):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/booking')
        else:
            messages.success(request, ("Username or Password error"))
            return redirect('shop')

    else:
        return render(request,"login.html")




