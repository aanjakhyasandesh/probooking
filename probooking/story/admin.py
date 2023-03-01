from django.contrib import admin
from .models import story,ourstory,story_description,empowering,meet_team,meet_team_pic,team_describe,team_image

# Register your models here.
admin.site.register(story)
admin.site.register(ourstory)
admin.site.register(story_description)
admin.site.register(empowering)
admin.site.register(meet_team)
admin.site.register(meet_team_pic)
admin.site.register(team_describe)
admin.site.register(team_image)
