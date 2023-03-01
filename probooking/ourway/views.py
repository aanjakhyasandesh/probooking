from django.shortcuts import render
from .models import our_way,ways_Describe
# Create your views here.
def ourway_view(request,*args,**kwargs):
    obj=our_way.objects.get(id=1)
    obje=ways_Describe.objects.all()
    context={
        'heading':obj.heading,
        'title':obj.title,
        'Second_heading':obj.Second_heading,
        'des':obje
    }
 
    print(obje)
    print(request.user)
    return render(request, "ourway.html",context)