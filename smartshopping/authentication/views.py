from django.shortcuts import render
import authentication.models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from .models import LoginForm


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

@csrf_protect
def login_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        errors = []
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('/')

                else:
                    errors.append('Incorrect username or password')

            else:
                errors.append('Invalid form')
        form = LoginForm()
        return render(request, "authentication/logIn.html", {
            'form': form,
            'errors': errors})
# def login_page(request):
#     if request.user.is_authenticated():
#         return redirect('/')
#     else:
#         form = LoginForm(data=request.POST or None)
#         if form.is_valid():
#             login(request, user)
#         return render(request, "authentication/logIn.html", {
#             'form': form})
