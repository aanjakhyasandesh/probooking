from django.contrib import admin
from .models import booking,booking_list,basketball,basketball_list,cricshal,cricshal_list,token,review

# Register your models here.
admin.site.register(booking)
# admin.site.register(booking_list)
admin.site.register(booking_list)
admin.site.register(review)
admin.site.register(basketball)
admin.site.register(basketball_list)
admin.site.register(cricshal)
admin.site.register(cricshal_list)
admin.site.register(token)