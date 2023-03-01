from django.shortcuts import render
from django.views.generic import DetailView, ListView
from booking.models import basketball,basketball_list
from django.http import HttpResponseRedirect

# from django.shortcuts import reverse

# # ,basketball,basketball_list,cricshal,cricshal_list
# # Create your views here.
class BasketDetailView(DetailView):
    model=basketball
    template_name='basketb.html'
    context_object_name='basketball'
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            # print("aaa")
            dates=request.POST['dates']
            hours=request.POST['hours']
            ampm=request.POST['ampm']
            try:
                phones=request.POST['phones']
            except MultiValueDictKeyError:
                phones = request.POST['phones']
            times=hours + ampm
            print(dates,times,phones)
            # BookingDetailView(ListView)
            basketball_list.objects.create(date=dates,time=times,phone=phones)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class BasketListView(ListView):
    model=basketball
    template_name='basketball.html'
    context_object_name='basketball'
    
