from django.shortcuts import render,redirect
from .models import booking,booking_list,review,token
from django.views.generic import DetailView, ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
import random
import string
# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError
# import datetime

def booking_delete(request,pk):
    if request.method == "POST":
        try:
            ids=request.POST['id']
            bookies=booking_list.objects.get(id=ids)
            if bookies==booking_list.objects.get(id=pk):
                messages.success(request, ("Super User ID Can't Delete It"))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                # print(id)
                print(bookies)
                bookies.delete()
                # bookies.save()
                messages.success(request, ("Booking Cancel Successful"))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        except:
                messages.success(request, ("Booking ID not Found"))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class BookingDetailView(DetailView):
    model=booking_list
    template_name='futsalbooking.html'
    context_object_name='book'
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            dates=request.POST['dates']
            hours=request.POST['hours']
            ampm=request.POST['ampm']
            try:
                phones=request.POST['phones']

            except MultiValueDictKeyError:
                phones = request.POST['phones']
            times=hours + ampm
            print(dates,times,phones)  
            booking_list.objects.create(date=dates,time=times,phone=phones)
            a=booking_list.objects.get(date=dates,time=times,phone=phones)
            b=a.id
            print(b)
            messages.success(request, ("Booking Done Successfully Your Booking Id: "f'{b}'))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            # return redirect('booking')

class BookingListview(ListView):
    model=booking
    template_name='booking.html'
    context_object_name='booking'


def get_review(request):
    obj=review.objects.all()
    context={
            'review':obj
        }
    if request.method == "POST":
        try:
            print(1)
            print(context)
            # try:
            reviews=request.POST.get("getreview")
            # except MultiValueDictKeyError:
            #     reviews=request.POST.get("getreview")
            review.objects.create(review=reviews)
            print(review.clean)
            return redirect('review')
        except:
            pass
    return render(request,'review.html',context)

def get_discount_token(request):
    list=[10,15,20,25,30,35,40,50,55,60,75,80,90,100]
    a=random.choice(list)
    b=string.ascii_letters
    b=random.choice(b)
    c=b+str(a)
    print(c)
    if request.method == "POST":
        token.objects.create(token=c)
        obj=token.objects.get(token=c)
        
        print(obj)
        return render(request,'discount.html',context)
    
    return render(request,'discount.html',context)

def view_booking(request):
    bookies=booking_list.objects.all().order_by('-id').values()
    context={
            'bookies':bookies,
        }
    return render(request,'viewbooking.html',context)



   