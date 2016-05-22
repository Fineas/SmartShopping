from django.shortcuts import render

from .models import LantMagazineForm, MagazinForm, UserForm

def lant(request):
    userform = UserForm(data=request.POST or None)
    lant_form = LantMagazineForm(data=request.POST or None)
    if request.method == 'POST':
        if lant_form.is_valid():
            userins = userform.save(commit = False)
            instance = lant_form.save(commit=False)
            instance.user_owner = userins
            instance.save()
            return redirect('/') 
    return render(request, 'magazin/lant.html', {
        'form': lant_form, 
        'userf': userform
    })
