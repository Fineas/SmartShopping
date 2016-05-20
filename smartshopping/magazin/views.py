from django.shortcuts import render

from .models import LantMagazineForm, MagazinForm

def lant(request):
    lant_form = LantMagazineForm(data=request.POST or None)
    if request.method == 'POST':
        if lant_form.is_valid():
            instance = lant_form.save(commit=False)
            instance.save()
    return render(request, 'magazin/lant.html', {
        'form': lant_form
    })
