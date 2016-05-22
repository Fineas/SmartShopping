from django.shortcuts import render
import authentication.models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from .models import LoginForm,RegisterForm


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

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

def register_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        errors = []
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                if User.objects.filter(username=username).exists():
                    errors.append("Username is already taken")
                password = form.cleaned_data['password']
                password2 = form.cleaned_data['password2']
                email = form.cleaned_data['email']
                if User.objects.filter(email=email).exists():
                    errors.append("Email is already taken")
                city = form.cleaned_data['city']
                country = form.cleaned_data['country']
                address = form.cleaned_data['address']
                phone = form.cleaned_data['phone']
                if password.isdigit():
                    errors.append("Password is entirely numeric")
                if password != password2:
                    errors.append("Passwords do not match")
                if len(password) < 8:
                    errors.append("Password is too short")
                if errors:
                    form = RegisterForm()
                    return render(request, "authentication/register.html", {
                        'form': form,
                        'errors': errors})
                new_user = User.objects.create_user(username, email, password)
                new_user.save()
                account = authentication.models.Account.objects.create(
                    user=new_user, city=city, country=country, address=address,
                    telefon=phone)
                account.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('/')
            else:
                errors.append("Invalid form")
    form = RegisterForm()
    return render(request, "authentication/register.html", {
                'form': form,
                'errors': errors})
