from django.shortcuts import render

from .models import OfertaForm


def oferta(request):
    oferta_form = OfertaForm(data=request.POST or None)
    if request.method == 'POST':
        if oferta_form.is_valid():
            instance = oferta_form.save(commit=False)
            instance.save()
    return render(request, 'magazin/lant.html', {
        'form': oferta_form
    })
