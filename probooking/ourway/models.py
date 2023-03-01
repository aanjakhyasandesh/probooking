from django.db import models

# Create your models here.

class our_way(models.Model):
    class Meta: verbose_name_plural = 'Our_Way'
    heading                 =models.CharField(max_length=30)
    title                   =models.CharField(max_length=30)
    Second_heading          =models.CharField(max_length=30)
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

class ways_Describe(models.Model):
    class Meta: verbose_name_plural = 'Ways_Describe'
    way_title            =models.CharField(max_length=15)
    way_description      =models.TextField(max_length=200)
    way_image            =models.ImageField(null=True, blank=True)