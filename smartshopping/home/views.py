from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    if request.user.is_authenticated():
         return render(request, 'home/home.html')
    else:
         return render(request, 'home/index.html')


def brandHome(request):
    return render(request,'home/home2.html')


