from django.shortcuts import render
from .models import contact
from django.core.mail import send_mail
# from django.core.mail import EmailMessage
from django.contrib import messages

# from django.views.decorators.csrf import csrf_protect
# Create your views here.
# @csrf_protect
def contact_view(request,*args,**kwargs):
    obj=contact.objects.get(id=1)
    context={
        'contact':obj.contact_heading,
        'address':obj.address,
        'office_type':obj.office_type,
        'email':obj. email,
        'support_email':obj.support_email,
        'office_type':obj.phone_office_type,
        'office_number':obj.phone_number,
        'office_type2':obj.phone_office_type2,
        'office_number2':obj.office_type2_number
    }
    if request.method == "POST":
        print("Hello")
        fname=request.POST['fname']
        femail=request.POST['femail']
        print(femail)
        fmessage=request.POST.get('fmessage')
        print(fmessage)
        data={
            'fname': fname,
            'femail':femail,
            'fmessage':fmessage

        }
        print(data)
        send_mail(data['fname'], data['fmessage'], '',[femail],fail_silently=False)
        # send_mail('khyaaanja@gmail.com', '{{fname}}', ['{{femail}}'])
        messages.success(request, ("Email Send Successfully"))
        
    # print(request.user)
    return render(request, "contact.html",context)