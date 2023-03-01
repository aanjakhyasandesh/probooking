from django.shortcuts import render
from .models import home,home_feature, notified,why_us,knitting,notified,leadership,testomonials
from contact.models import map_intergration
# Create your views here.
def home_view(request,*args,**kwargs):
    ob=home.objects.all()
    obj=home_feature.objects.get(id=1)
    obje=why_us.objects.get(id=1)
    objec=knitting.objects.get(id=1)
    object1=notified.objects.get(id=1)
    # leader=leadership.objects.all()
    testomonial=testomonials.objects.all()
    map=map_intergration.objects.all()
    context={
        'home':ob,
        'feature_title':obj.feature_title,
        'feature_type1':obj.feature_type1,
        'feature_type2':obj.feature_type2,
        'feature_type3':obj.feature_type3,
        'whyus_title':obje.whyus_title,
        'whyus_description':obje.whyus_description,
        'whyus_bg':obje.whyus_bg,
        'knitting_title':objec.knitting_title,
        'knitting_description':objec.knitting_description,
        'knitting_image':objec.knitting_image,
        'knitting_background':objec.knitting_background,
        'heading':object1.heading,
        'description':object1.description,
        'notified_bg':object1.notified_bg,
        # 'leadership':leader,
        'testomonial':testomonial,
        'map':map
        
    }
    
    return render(request, "home.html",context)