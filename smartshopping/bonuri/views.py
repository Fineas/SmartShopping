from django.shortcuts import render

# Create your views here.

def bonuri(request):
    return render(request,'bonuri/bonuri.html')
