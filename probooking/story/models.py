from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.
class story(models.Model):
    class Meta: verbose_name_plural="story Homepage"
    storypage_image=models.ImageField(blank=True, null=True)
    storypage_title=models.CharField(max_length=50)
    storypage_description=models.CharField(max_length=50)
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)
    

class ourstory(models.Model):
    ourstory                    =models.CharField(max_length=50)
    ourstory_description        =models.TextField() 
    ourstory_lastdescription    =models.TextField()
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

class story_description(models.Model):
    class Meta: verbose_name_plural="Story with Description"
    story_title=models.CharField(max_length=50)
    story_description=models.TextField()
    story_image=models.ImageField()

class empowering(models.Model):
    class Meta: verbose_name_plural='Empowering Section'
    empower                    =models.CharField(max_length=50)
    empower_description        =models.TextField()
    up_left                    =models.ImageField(null=True, blank=True)
    up_right                   =models.ImageField(null=True, blank=True)
    down_left                  =models.ImageField(null=True, blank=True)
    down_right                 =models.ImageField(null=True, blank=True)
    empower_background          =models.ImageField(null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

class meet_team(models.Model):
    class Meta: verbose_name_plural="Meet Our Team"
    meet_team=models.CharField(max_length=50)
    meet_description=models.CharField(max_length=50)
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

class meet_team_pic(models.Model):
    class Meta: verbose_name_plural="Meet Team Image"
    meet_team_image=models.ImageField(blank=True,null=True)
    name=models.CharField(max_length=20,blank=True)
    post=models.CharField(max_length=20,blank=True)

class team_describe(models.Model):
    class Meta: verbose_name_plural="Team Description"
    our_team=models.CharField(max_length=50)
    team_description=models.CharField(max_length=50)
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

class team_image(models.Model):
    class Meta: verbose_name_plural='Team Image'
    team_image=models.ImageField(blank=True,null=True)
