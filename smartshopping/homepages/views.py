from django.shortcuts import render

# Create your views here.

def home(request):
    if request.user.is_authenticated():
         return render(request, 'homepages/home.html')
    else:
         return render(request, 'homepages/index.html')



