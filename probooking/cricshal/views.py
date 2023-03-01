from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.http import HttpResponseRedirect
from booking.models import cricshal,cricshal_list
# Create your views here.
class CricshalDetailView(DetailView):
    model=cricshal
    template_name='cricshalbook.html'
    context_object_name='cricshal'
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
            cricshal_list.objects.create(date=dates,time=times,phone=phones)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
class CricshalListView(ListView):
    model=cricshal
    template_name='cricshal.html'
    context_object_name='cricshal'