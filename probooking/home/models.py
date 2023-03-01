from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class home(models.Model):
    class Meta: verbose_name_plural='home_slider'
    slider      =models.ImageField(null=True, blank=True)
    slider_title=models.CharField(max_length=50)
    landing_description1=models.TextField()

class home_feature(models.Model):
    class Meta: verbose_name_plural = 'home_feature'
    feature_title       =models.CharField(max_length=15)
    feature_type1       =models.CharField(max_length=15)
    feature_type2       =models.CharField(max_length=15)
    feature_type3       =models.CharField(max_length=15)
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

class why_us(models.Model):
    class Meta: verbose_name_plural = 'why_us'
    whyus_title         =models.CharField(max_length=10)
    whyus_description   =models.TextField()
    whyus_bg            =models.ImageField(null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)


class knitting(models.Model):
    class Meta: verbose_name_plural = 'knitting'
    knitting_title          =models.CharField(max_length=25)
    knitting_description    =models.TextField()
    knitting_image          =models.ImageField(null=True, blank=True)
    knitting_background     =models.ImageField(null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

class gallery(models.Model):
    class Meta: verbose_name_plural = 'gallery'
    gallery_description       =models.TextField(max_length=70)
    image1                  =models.ImageField(null=True, blank=True)
    image2                  =models.ImageField(null=True, blank=True)
    image3                  =models.ImageField(null=True, blank=True)
    image4                  =models.ImageField(null=True, blank=True)

class notified(models.Model):
    class Meta: verbose_name_plural = 'notified'
    heading    =models.CharField(max_length=50)
    description=models.TextField()
    notified_bg=models.ImageField(null=True, blank=True)

class leadership(models.Model):
    class Meta: verbose_name_plural = 'leadership'
    image=models.ImageField(null=True, blank=True)
    leader_name=models.CharField(max_length=25)
    leader_position=models.CharField(max_length=25)
    facebook_link=models.CharField(max_length=500,blank=True,null=True)
    twitter_link=models.CharField(max_length=500,blank=True,null=True)
    linkedln_link=models.CharField(max_length=500,blank=True,null=True)
    instagram_link=models.CharField(max_length=500,blank=True,null=True)


class testomonials(models.Model):
    class Meta: verbose_name_plural ="testomonial"
    image=models.ImageField(null=True,blank=True)
    description=models.TextField()
    name=models.CharField(max_length=25)