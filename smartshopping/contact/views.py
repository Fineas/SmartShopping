from django.shortcuts import render
from .models import Contact

# Create your views here.
def contact(request):

    if request.method == 'POST':
        frist_name=request.POST.get('icon_prefix')
        phone=request.POST.get('icon_telephone')
        message = request.POST.get('message')
        contact = Contact.objects.create(frist_name = frist_name, phone=phone, message=message)
        contact.save()
        return render(request, 'contact/contact.html',{'error': 'Message is send'})

    return render(request,'contact/contact.html')