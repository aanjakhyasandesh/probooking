from django.db import models

# Create your models here.
class contact(models.Model):
    contact_heading =models.CharField(max_length=50, blank=True)
    address         = models.CharField(max_length=50,blank=True)
    office_type     = models.CharField(max_length=50,blank=True)
    email           = models.CharField(max_length=50,blank=True)
    support_email   =models.CharField(max_length=50,blank=True)
    phone_office_type=models.CharField(max_length=15,blank=True)
    phone_number    =models.CharField(max_length=13,blank=True)
    phone_office_type2=models.CharField(max_length=15,blank=True)
    office_type2_number=models.CharField(max_length=13,blank=True)
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)


class map_intergration(models.Model):
    longitude =models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    latitude =models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    name=models.CharField(max_length=20,blank=True,null=True)