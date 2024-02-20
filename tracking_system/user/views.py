from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignUpUserForm, LoginUserForm
from django.contrib import messages


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('login')
    else:
        form = SignUpUserForm()
    return render(request, 'user/sign-up.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Пользователь не найден')
    form = LoginUserForm()
    return render(request, 'user/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')
