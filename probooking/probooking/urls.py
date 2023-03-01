"""handicraft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import home_view
from story.views import story_view
from ourway.views import ourway_view
from contact.views import contact_view
from booking.views import BookingDetailView,BookingListview,booking_delete,get_review,get_discount_token,view_booking
from basketball.views import BasketDetailView,BasketListView
from cricshal.views import CricshalListView,CricshalDetailView                         
from shop.views import  shop_view
from preloader.views import preloader_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'), 
    path('story/',story_view,name='story'),
    path('ourway/', ourway_view, name='our_way'), 
    path('contact/', contact_view, name='contact'),
    path('booking/', BookingListview.as_view(), name='booking_view'),
    path('booking/<int:pk>', BookingDetailView.as_view(), name='bookingdetail'),
    path('review/', get_review, name='review'),
    path('viewbooking/', view_booking, name='viewbooking'),
    path('discoupon/', get_discount_token, name='discoupon'),
    path('booking/<int:pk>/delete', booking_delete, name='bookingdelete'),
    path('basketball/', BasketListView.as_view(), name='basket_view'),
    path('basketball/<int:pk>', BasketDetailView.as_view(), name='basketdetail'),
    path('cricshal/', CricshalListView.as_view(), name='cricshal_view'),
    path('cricshal/<int:pk>', CricshalDetailView.as_view(), name='cricshaldetail'),
    path('shop/', shop_view, name='shop'),
    path('shop/', include('django.contrib.auth.urls')),
    path('preloader/', preloader_view,name='preloader'),
    path('admin/', admin.site.urls),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 