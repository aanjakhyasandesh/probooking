from django.db import models
# from django.shortcuts import reverse
import datetime
# # Create your models here.
class booking(models.Model):
    class Meta: verbose_name_plural='booking'
    id=models.IntegerField(primary_key=True)
    booking_image      =models.ImageField()
    booking_title=models.CharField(max_length=50)
    booking_description        =models.TextField(null=True)
    
class booking_list(models.Model):
    class Meta: verbose_name_plural='bookinglist'
    phone=models.CharField(max_length=14)
    date=models.CharField(max_length=12)
    time=models.CharField(max_length=8)
    book=models.ForeignKey(booking,on_delete=models.CASCADE,blank=True,null=True)
    

class review(models.Model):
    class Meta: verbose_name_plural='Reviews'
    review=models.TextField(null=True)

class basketball(models.Model):
    class Meta: verbose_name_plural='basketball'
    id=models.IntegerField(primary_key=True)
    booking_image      =models.ImageField(null=True, blank=True)
    booking_title=models.CharField(max_length=50)
    booking_description        =models.TextField(null=True)
    
class basketball_list(models.Model):
    class Meta: verbose_name_plural='basketballlist'
    phone=models.CharField(max_length=14)
    date=models.CharField(max_length=12)
    time=models.CharField(max_length=8)

class cricshal(models.Model):
    class Meta: verbose_name_plural='cricshal'
    id=models.IntegerField(primary_key=True)
    booking_image      =models.ImageField(null=True, blank=True)
    booking_title=models.CharField(max_length=50)
    booking_description        =models.TextField(null=True)
    
class cricshal_list(models.Model):
    class Meta: verbose_name_plural='cricshallist'
    phone=models.CharField(max_length=14)
    date=models.CharField(max_length=12)
    time=models.CharField(max_length=8)
    
# class discount_token(models.Model):
#     token=models.CharField(max_length=50)

class token(models.Model):
    token=models.CharField(max_length=4)