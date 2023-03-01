from django.contrib import admin
from .models import home,home_feature, notified,why_us,knitting,gallery,notified,testomonials
# Register your models here.
admin.site.register(home)
admin.site.register(home_feature)
admin.site.register(why_us)
admin.site.register(knitting)
admin.site.register(gallery)
admin.site.register(notified)
# admin.site.register(leadership)
admin.site.register(testomonials)
