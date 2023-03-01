from django.db import models

# Create your models here.
class basketball(models.Model):
    class Meta: verbose_name_plural='basketball'
    id=models.IntegerField(primary_key=True)
    booking_image      =models.ImageField(null=True, blank=True)
    booking_title=models.CharField(max_length=50)
    booking_description        =models.TextField(null=True)
    
class basketball_list(models.Model):
    class Meta: verbose_name_plural='basketballlist'
    date=models.CharField(max_length=12)
    time=models.CharField(max_length=8)