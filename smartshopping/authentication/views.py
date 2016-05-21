from django.shortcuts import render
import authentication.models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

from .models import LoginForm


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def login_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        form = LoginForm(data=request.POST or None)
        if form.is_valid():
            login(request, user)
        return render(request, "authentication/logIn.html", {
            'form': form})
