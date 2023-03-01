from django.shortcuts import render
from .models import story,ourstory,story_description,empowering,meet_team,meet_team_pic,team_describe,team_image
# Create your views here.
def story_view(request,*args,**kwargs):
    storys=story.objects.get(id=1)
    our=ourstory.objects.get(id=1)
    story_describe=story_description.objects.all()
    empower=empowering.objects.get(id=1)
    meet=meet_team.objects.get(id=1)
    meet_pic=meet_team_pic.objects.all()
    describe=team_describe.objects.get(id=1)
    team_pic=team_image.objects.all()

    context={
        'storypage_image':storys.storypage_image,
        'storypage_title':storys.storypage_title,
        'storypage_description':storys.storypage_description,
        'ourstory':our.ourstory,
        'ourstory_description':our.ourstory_description,
        'ourstory_lastdescription':our.ourstory_lastdescription,
        'story':story_describe,
        'empower':empower.empower,
        'empower_description':empower.empower_description,
        'up_left':empower.up_left,
        'up_right':empower.up_right,
        'down_left':empower.down_left,
        'down_right':empower.down_right,
        'empower_background':empower.empower_background,
        'meet_team':meet.meet_team,
        'meet_description':meet.meet_description,
        'meet_image':meet_pic,
        'our_team':describe.our_team,
        'team_description':describe.team_description,
        'team_image':team_pic
    }
    print(empower.empower_background)
    return render(request, "story.html",context)
